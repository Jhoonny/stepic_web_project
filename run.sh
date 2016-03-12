#!/usr/bin/env bash
sudo /etc/init.d/nginx stop
sudo python ~/web/ask/manage.py runserver 0.0.0.0:80