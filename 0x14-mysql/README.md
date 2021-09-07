Exercises for the Project 0x14. MySQL

Installing MySQL:

echo 'deb http://repo.mysql.com/apt/ubuntu/ trusty mysql-5.7-dmr' | sudo tee -a /etc/apt/sources.list
sudo apt-get update
sudo apt-get install mysql-server-5.7

Default user is root, choose a password it can be root too

mysql -h localhost -u root -p
CREATE USER IF NOT EXISTS 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
FLUSH PRIVILEGES;
quit
