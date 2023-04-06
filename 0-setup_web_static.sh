#!/usr/bin/env bash
#a Bash script that sets up your web servers for the deployment
# of web_static
#!/usr/bin/env bash

# Install Nginx if not already installed
if [ ! -x "$(command -v nginx)" ]; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create necessary folders if they don't already exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file for testing
sudo echo "<html>
  <head>
  <title>Test Page</title>
  </head>
  <body><p>This is a test.</p></body>
  </html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symbolic link to the test folder
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i 's|^\(\s*location / {\)|\1\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n|' /etc/nginx/sites-available/default

# Restart Nginx to apply the changes
sudo service nginx restart
