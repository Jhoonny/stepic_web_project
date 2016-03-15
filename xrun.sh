#!/usr/bin/env bash
echo "Start and ini myqsl ..."
sudo touch /var/run/mysqld/mysqld.sock
sudo chown -R mysql /var/run/mysqld
sudo /etc/init.d/mysql restart

sudo mysql -uroot -e "create database if not exists ask_db"
#sudo mysql -uroot -e ""
sudo mysql -uroot -e "grant all on ask_db.* to 'ask_user'@'localhost' identified by 'ask_pwd'"

python /home/box/web/ask/manage.py syncdb
python /home/box/web/ask/manage.py validate

sudo /etc/init.d/nginx stop
sudo python ~/web/ask/manage.py runserver 0.0.0.0:80