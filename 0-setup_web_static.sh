#!/usr/bin/env bash
# setting up webstatic dependency direcotories

folders=("data" "/data/web_static" "/data/web_static/releases"
        "/data/web_static/shared/" "/data/web_static/releases/test/")

files=("/data/web_static/releases/test/index.html")

for folder in "${folders[@]}"; do
        if [ ! -d "$folder" ]; then
                sudo mkdir -p "$folder"
        fi
done

for file in "${files[@]}"; do
        if [ -f "$file" ]; then
                sudo rm "$file"
        fi
        sudo touch "$file"
        echo "Hello World!!!" | sudo tee -a "$file"
	new_content=$(cat <<'EOF'
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOF
)

# Write the new HTML content to the file
echo "$new_content" | sudo tee "$file" > /dev/null
done

link="/data/web_static/current"
target="/data/web_static/releases/test"

if [ -L "$link" ]; then
    rm "$link"
fi
ln -sfn "$target" "$link"

sudo chown -R ubuntu:ubuntu /data

nginx_config="/etc/nginx/sites-available/default"

# Comment out the existing content in the Nginx configuration file
sudo sed -i 's/^/# /' "$nginx_config"

# Define the new Nginx configuration
new_config=$(cat <<'EOF'
server {
    # ... other configurations ...
        listen 80;
        listen [::]:80;

        root /data/web_static/current;
#       root /var/www/html;

    location /hbnb_static/ {
        alias /data/web_static/current/;
        index index.html;
    }
}
EOF
)

# Append the new configuration to the Nginx configuration file
echo "$new_config" | sudo tee -a "$nginx_config" > /dev/null

sudo service nginx restart
