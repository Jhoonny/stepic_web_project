#!/usr/bin/env bash

sudo /etc/init.d/mysql start
mysql -uroot -e "CREATE DATABASE ask_db"
mysql -uroot -e "CREATE USER 'ask'@'localhost' IDENTIFIED BY PASSWORD 'YES'"
mysql -uroot -e "GRANT ALL ask_db.* TO 'ask'@'localhost' IDENTIFIED BY PASSWORD 'YES'"
sudo /etc/init.d/mysql restart
python /home/box/web/ask/manage.py syncdb
python /home/box/web/ask/manage.py validate
