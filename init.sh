#!/usr/bin/env bash

# /home/box/web

sudo ﻿ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart

#git clone https://github.com/Jhoonny/stepic_web_project.git /home/box/web
#bash /home/box/web/init.sh