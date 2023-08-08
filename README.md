# RUMBA
Real User Simulation for Web App Testing/LoadGen

This is a script to simulate real user load against a web application.

For this script to run a number of dependencies need to first be installed and updated.

The script can then be run on startup, or be controlled via a second script to allow for periodic recource cleanup.

Instructions follow (And will be rewritten in a way that makes sense shortly):

Making loadgen work in ubuntu
```
sudo apt-get update
sudo apt install python3-pip
sudo pip3 install pyppeteer
sudo apt-get install chromium-chromedriver

sudo apt install -y gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget
  
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt update 
sudo apt install google-chrome-stable
    
sudo mkdir /opt/bots_load_gen
```  
Copy the following files to `/opt/bot_load_gen`
```
boot_start.sh 
nav_matrix.py
real_user_simulator.py
snap_remover.sh
user_agents.py
```
  
Copy `crontab4bots_datagen.txt` to crontab -e

