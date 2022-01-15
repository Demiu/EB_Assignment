#!/bin/bash

echo "Creating user and database"
mysql -pstudent < /tmp/be_171974/make_database.sql
echo "Loading backup..."
mysql -uBE_171974 -ppassword BE_171974_DB < /tmp/be_171974/backup.sql

echo "Cleaning up files..."
rm -rf /tmp/be_171974

