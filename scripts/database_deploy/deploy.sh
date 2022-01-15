#!/bin/bash

CONTROL_MASTER_SOCKET="/tmp/ssh_tunnel_%r_%h"

echo "Making tunnel..."
ssh -f -N -L 5242:actina15.maas:22 rsww@172.20.83.101 -S $CONTROL_MASTER_SOCKET

echo "Copying files..."
scp -P 5242 -r in_cluster/* ../../db-dumps/backup.sql hdoop@localhost:/mnt/block-storage/students/projects/students-swarm-services/BE_171974

echo "Running script in cluster..."
ssh -p 5242 -t hdoop@localhost 'sudo /mnt/block-storage/students/projects/students-swarm-services/BE_171974/deploy_in_cluster.sh'

echo "Shutting down tunnel..."
ssh -O exit -S $CONTROL_MASTER_SOCKET rsww@172.20.83.101

