#!/usr/bin/env bash

sudo touch /var/run/mysqld/mysqld.sock
sudo chown -R mysql /var/run/mysqld
sudo /etc/init.d/mysql restart
sudo mysqlcheck --check-upgrade --all-databases --auto-repair -u root -p
sudo mysql_upgrade --force -u root -p
