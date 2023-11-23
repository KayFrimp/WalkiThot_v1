-- prepares a MySQL server for the WALKITHOT project

CREATE DATABASE IF NOT EXISTS walki_dev_db;
CREATE USER IF NOT EXISTS 'walki_dev'@'localhost' IDENTIFIED BY 'walki_dev_pwd';
GRANT ALL PRIVILEGES ON `walki_dev_db`.* TO 'walki_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'walki_dev'@'localhost';
FLUSH PRIVILEGES;