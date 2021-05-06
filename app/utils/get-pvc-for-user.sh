#!/bin/bash


USERNAME=$1
NAMESPACE=$2

PVC=$(kubectl get pv --namespace=$NAMESPACE | grep "\b$NAMESPACE/claim-$USERNAME\b" | cut -d " " -f1)

if [ -z "$PVC" ]
then
    >&2 echo "User not found: $USERNAME"
    exit 1
else
    HDD=$(kubectl describe pv --namespace=$NAMESPACE $PVC | grep PDName | rev | cut -d " " -f1 | rev)

    echo "{\"PVC\": \"$PVC\", \"HDD\": \"$HDD\"}"
fi

exit 0



