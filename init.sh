sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default

cd /home/box/web/
gunicorn -b 0.0.0.0:8080 -D hello:app

cd /home/box/web/ask/
gunicorn ask.wsgi:application --bind 0.0.0.0:8000 -D

sudo /etc/init.d/nginx restart
