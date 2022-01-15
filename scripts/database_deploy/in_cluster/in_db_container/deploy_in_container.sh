#!/bin/bash

mysql -pstudent < /tmp/be_171974/make_database.sql
mysql -uBE_171974 -ppassword BE_171974_DB < /tmp/be_171974/backup.sql

