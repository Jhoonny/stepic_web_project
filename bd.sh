#!/usr/bin/env bash

sudo /etc/init.d/mysql restart
mysql -uroot -e "CREATE DATABASE qa"
mysql -uroot -e "CREATE USER 'qa'@'localhost' IDENTIFIED BY PASSWORD 'qa'"
mysql -uroot -e "GRANT ALL qa.* TO 'qa'@'localhost'"

python /home/box/web/ask/manage.py syncdb
python /home/box/web/ask/manage.py validate
