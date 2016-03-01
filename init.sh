#!/usr/bin/env bash
# ini file for work

# При входе в терминал надо запустить Ngnix и проверить:
sudo /etc/init.d/nginx start
# ps -o pid,euser,egroup,comm,args -C nginx

sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo /etc/init.d/gunicorn restart
