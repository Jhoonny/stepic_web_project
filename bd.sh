#!/usr/bin/env bash

mysql -u root -e "create database db_qa"

cd ask
./manage.py syncdb
./manage.py validate
