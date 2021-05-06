#!/bin/bash

USERNAME=$1
VMNAME=$2
DATALOC=$3


loc=$DATALOC/$USERNAME

# un-mount the disk
echo 'Unmounting disk'
mnt=$(sudo umount $loc)
if [ $? -ne 0 ]; then
    >&2 echo "Error during disk un-mounting"
    exit 1
fi

echo 'Detaching disk'
detach=$(gcloud compute instances detach-disk $VMNAME --device-name $USERNAME)
if [ $? -ne 0 ]; then
    >&2 echo "Error while detaching the disk"
    exit 1
fi

# clean up
echo 'Cleaning up userspace'
rm -rf $loc

exit 0



