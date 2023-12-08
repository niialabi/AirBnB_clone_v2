#!/usr/bin/env bash
# B_script that sets web_static.
sudo apt-get update
sudo apt-get -y install nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo 'Hello Africa' > /data/web_static/releases/test/index.html
ln -sfn /data/web_static/releases/test /data/web_static/current
chown -R ubuntu:ubuntu /data/
tag="server_name _;"
c_tag="server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "s|$tag|$c_tag|" /etc/nginx/sites-available/default
sudo service nginx restart
