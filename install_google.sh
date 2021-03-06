#!/usr/bin/env bash
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install -y python3-pip
sudo apt-get install build-essential libssl-dev libffi-dev python-dev -y
sudo apt-get install python3-bs4 -y

sudo apt-get install -y unzip openjdk-8-jre-headless xvfb libxi6 libgconf-2-4
sudo apt-get install python3-pip -y
sudo pip3 install --upgrade pip
sudo pip3 install selenium
sudo pip install xvfbwrapper
sudo apt-get install xvfb x11-xkb-utils -y

wget https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
rm -f chromedriver_linux64.zip
sudo mv -f chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod 0755 /usr/local/bin/chromedriver

wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update 
sudo apt-get install google-chrome-stable -y

