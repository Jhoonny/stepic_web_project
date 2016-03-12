#!/usr/bin/env bash

sudo apt-get update
#sudo apt-get remove python-django
sudo pip3 install django
sudo pip3 install gunicorn
sudo apt-get install python3-dev libmysqlclient-dev
sudo pip3 install mysqlclient

sudo mysqld &
echo "Creade db .."
sudo mysql -uroot -e "create database if not exists ask"
#sudo mysql -uroot -e "grant all on ask.* to 'as'@'localhost' identified by 'as'"
echo "Sync db ..."
python3 /home/box/web/ask/manage.py migrate
sudo /etc/init.d/nginx stop
sudo python3 ~/web/ask/manage.py runserver 0.0.0.0:80

