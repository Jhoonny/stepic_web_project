#!/usr/bin/env bash

# /home/box/web

# При входе в терминал надо запустить Ngnix и проверить:
# sudo /etc/init.d/nginx start
# ps -o pid,euser,egroup,comm,args -C nginx

#sudo ﻿ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf

sudo ln -sf /home/box/web/etc/nginx3.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/gunicor.conf
#sudo /etc/init.d/gunicorn restart

#git clone https://github.com/Jhoonny/stepic_web_project.git /home/box/web
#bash /home/box/web/init.sh