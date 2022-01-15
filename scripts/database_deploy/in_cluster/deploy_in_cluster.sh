#!/bin/bash

cd "$(dirname "$0")"

MYSQL_ID=$(docker ps -q -f name=admin-mysql_db)

echo "Found mysql container $MYSQL_ID"

echo "Copying files..."
docker exec $MYSQL_ID mkdir -p /tmp/be_171974
docker cp in_db_container/. $MYSQL_ID:/tmp/be_171974/
docker cp backup.sql $MYSQL_ID:/tmp/be_171974/

echo "Running script in container..."
docker exec $MYSQL_ID /tmp/be_171974/deploy_in_container.sh

