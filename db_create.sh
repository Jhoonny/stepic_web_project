#!/usr/bin/env bash

#sudo /etc/init.d/mysql start
#sudo mysql -uroot -e "CREATE DATABASE ask"
#sudo mysql -uroot -e "CREATE USER 'ask'@'localhost' IDENTIFIED BY 'YES'"
#sudo mysql -uroot -e "GRANT ALL ask_db.* TO 'ask'@'localhost' IDENTIFIED BY 'YES'"
#sudo /etc/init.d/mysql restart
#python /home/box/web/ask/manage.py syncdb
#python /home/box/web/ask/manage.py validate

#sudo mysqld &
echo "Creade db .."
sudo mysql -uroot -e "create database if not exists ask"
#sudo mysql -uroot -e "grant all on ask.* to 'as'@'localhost' identified by 'as'"
echo "Sync db ..."
python /home/box/web/ask/manage.py syncdb
python /home/box/web/ask/manage.py validate