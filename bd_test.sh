#!/usr/bin/env bash

sudo touch /var/run/mysqld/mysqld.sock
sudo chown -R mysql /var/run/mysqld
sudo /etc/init.d/mysql restart