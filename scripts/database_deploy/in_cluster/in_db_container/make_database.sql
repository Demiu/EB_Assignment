CREATE DATABASE IF NOT EXISTS BE_171974_DB;
CREATE USER IF NOT EXISTS BE_171974@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON BE_171974_DB.* TO 'BE_171974'@'%';
FLUSH PRIVILEGES;
