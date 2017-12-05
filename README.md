# selenium

sudo apt-get update
sudo apt-get -y upgrade
python3 -V
sudo apt-get install -y python3-pip
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
pip install selenium

wget -q -O https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip
unzip ~/chromedriver_linux64.zip -d ~/
rm ~/chromedriver_linux64.zip
sudo mv -f ~/chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod 0755 /usr/local/bin/chromedriver



wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update 
sudo apt-get install google-chrome-stable


http://www.discoversdk.com/blog/web-scraping-with-selenium

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

url = "http://www.phptravels.net/login"
username = "user@phptravels.com"
password = "demouser"
driver = webdriver.Chrome()

if __name__ == "__main__":
   driver.get(url)

   uname = driver.find_element_by_name("username") ← find by element name
   uname.send_keys(username)  ← enters the username in textbox

   passw = driver.find_element_by_name("password")
   passw.send_keys(password)  ← enters the password in textbox
   

   # Find the submit button using class name and click on it.
   submit_button = driver.find_element_by_class_name("loginbtn").click()
