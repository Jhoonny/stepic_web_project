#!/usr/bin/env bash

#sudo /etc/init.d/mysql start
#sudo mysql -uroot -e "CREATE DATABASE ask_db"
#sudo mysql -uroot -e "CREATE USER 'ask'@'localhost' IDENTIFIED BY PASSWORD 'YES'"
#sudo mysql -uroot -e "GRANT ALL ask_db.* TO 'ask'@'localhost' IDENTIFIED BY PASSWORD 'YES'"
#sudo /etc/init.d/mysql restart
#python /home/box/web/ask/manage.py syncdb
#python /home/box/web/ask/manage.py validate

#sudo mysqld &

sudo mysql -uroot -e "create database if not exists ask_db"
sudo mysql -uroot -e "grant all on ask_db.* to 'as'@'localhost' identified by 'as'"

python /home/box/web/ask/manage.py syncdb
python /home/box/web/ask/manage.py validate