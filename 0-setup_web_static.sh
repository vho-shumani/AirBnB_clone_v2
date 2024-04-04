#!/usr/bin/env bash
#Install Nginx if it not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create the folder /data/web_static/shared
# Create the folder /data/web_static/releases/test/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
# Create a fake HTML file /data/web_static/releases/test/index.html
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html 

# Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group.
sudo chown -R ubuntu:ubuntu /data

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static)
sudo sed -i '/^server_name _;/ a\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# test if configuration is successfull and restarts nginx.
sudo nginx -t
sudo service nginx restart

