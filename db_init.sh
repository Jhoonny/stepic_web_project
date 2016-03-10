#!/usr/bin/env bash

sudo touch /var/run/mysqld/mysqld.sock
sudo chown -R mysql /var/run/mysqld
sudo /etc/init.d/mysql restart
mysqlcheck --check-upgrade --all-databases --auto-repair -u root -p
mysql_upgrade --force -u root -p
