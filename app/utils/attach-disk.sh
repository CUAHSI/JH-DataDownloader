#!/bin/bash


USERNAME=$1
DISK=$2
ZONE=$3
VMNAME=$4
DATALOC=$5

echo 'Attaching disk'
attach=$(gcloud compute instances attach-disk $VMNAME --disk $DISK --device-name $USERNAME --zone $ZONE)

if [ $? -ne 0 ]; then
    >&2 echo "Error while attaching pvc"
    exit 1
fi

# get disk name
echo 'Acquiring disk name'
diskname=$(ls -l /dev/disk/by-id/ | grep $USERNAME | awk 'NR==1{print $9}')
if [ -z $diskname ]; then
    >&2 echo "Disk not found for $USERNAME"
    exit 1
fi

# get disk path
echo 'Getting disk path'
diskloc=$(readlink -f /dev/disk/by-id/$diskname)

# mkdir for user
echo 'Preparing userspace'
loc=$DATALOC/$USERNAME
rm -rf $loc
mkdir -p $loc

# mount the disk path
echo 'Mounting disk'
mnt=$(sudo mount $diskloc $loc)
if [ $? -ne 0 ]; then
    >&2 echo "Error during disk mounting"
    exit 1
fi

# compress the data, excluding hidden dirs and several known dirsa
echo 'Compressing data'
tar -C $DATALOC \
    --exclude=conda-envs \
    --exclude=lost+found \
    --exclude=".*" \
    -czf $DATALOC/$USERNAME.tar.gz $USERNAME

echo 'done'
echo $DATALOC/$USERNAME.tar.gz

exit 0



