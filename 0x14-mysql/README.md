Exercises for the Project 0x14. MySQL

# Steps to follow in the 2 servers Master and Slave
## TASk0
Installing MySQL:
```bash
echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get install mysql-server-5.7
```
## TASk1
Default user is root, choose a password it can be root too
```mysql
mysql -h localhost -u root -p
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
FLUSH PRIVILEGES;
quit
```
```bash
sudo mysql -h localhost -u root -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost';"
```
## TASk2
```mysql
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (id INT(10) NOT NULL  AUTO_INCREMENT, name VARCHAR(30), PRIMARY KEY (id));
GRANT ALL PRIVILEGES ON tyrell_corp.* TO 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
```

Only in Server 1
```mysql
INSERT INTO nexus6 (name) VALUES ('Leon');
```
## TASk3
```mysql
SELECT * FROM NEXUS6
CREATE USER IF NOT EXISTS 'replica_user'@'%' IDENTIFIED BY 'root';
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%' IDENTIFIED BY 'root';
FLUSH PRIVILEGES;
```
Configure your file /etc/mysql/mysql.conf.d/mysqld.cnf
The line bind-address must be commented
```bash
	#bind-address            =127.0.0.1
	server-id               = 1
	log_bin                 = /var/log/mysql/mysql-bin.log
	binlog_do_db            = tyrell_corp
```
```bash
sudo service mysql restart
```
```mysql
USE tyrell_corp;
FLUSH TABLES WITH READ LOCK;
SHOW MASTER STATUS;
```
```bash
sudo ufw allow 3306

mysqldump -uholberton_user -p --opt tyrell_corp > tyrell_corp.sql
```
UNLOCK TABLES;

CHANGE MASTER TO MASTER_HOST='34.75.111.103',MASTER_USER='replica_user', MASTER_PASSWORD='root', MASTER_LOG_FILE='mysql-bin.000001', MASTER_LOG_POS=154;


