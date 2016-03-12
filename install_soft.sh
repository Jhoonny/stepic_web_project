#!/usr/bin/env bash

sudo apt-get update
sudo apt-get remove python-django
sudo pip3 install django
sudo pip3 install gunicorn
sudo apt-get install python3-dev libmysqlclient-dev
sudo pip3 install mysqlclient

