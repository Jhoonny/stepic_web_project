#!/usr/bin/env bash

# /home/box/web

# При входе в терминал надо запустить Ngnix и проверить:
sudo /etc/init.d/nginx start
ps -o pid,euser,egroup,comm,args -C nginx
