# selenium

sudo apt-get update
sudo apt-get -y upgrade
python3 -V
sudo apt-get install -y python3-pip
sudo apt-get install build-essential libssl-dev libffi-dev python-dev

sudo apt-get install -y unzip openjdk-8-jre-headless xvfb libxi6 libgconf-2-4
sudo apt-get install python3-pip
pip3 install --upgrade pip
pip3 install selenium

wget https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip

wget -q -O https://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip
unzip ~/chromedriver_linux64.zip -d ~/
rm ~/chromedriver_linux64.zip
sudo mv -f ~/chromedriver /usr/local/bin/chromedriver
sudo chown root:root /usr/local/bin/chromedriver
sudo chmod 0755 /usr/local/bin/chromedriver

https://raw.githubusercontent.com/ildarcheg/selenium/master/install.sh




wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' | sudo tee /etc/apt/sources.list.d/google-chrome.list
sudo apt-get update 
sudo apt-get install google-chrome-stable

sudo add-apt-repository ppa:webupd8team/sublime-text-3
sudo apt-get update
sudo apt-get install -y sublime-text-installer

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

   uname = driver.find_element_by_name("username")
   uname.send_keys(username)

   passw = driver.find_element_by_name("password")
   passw.send_keys(password)
   

   # Find the submit button using class name and click on it.
   submit_button = driver.find_element_by_class_name("loginbtn").click()






import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

url = "http://www.forum.mista.ru/index.php"
username = "Добрый хачик"
password = "11"
driver = webdriver.Chrome()

if __name__ == "__main__":
   driver.get(url)

   uname = driver.find_element_by_name("user_name")
   uname.send_keys(username)

   passw = driver.find_element_by_name("user_password")
   passw.send_keys(password)
   

   # Find the submit button using class name and click on it.
   submit_button = driver.find_element_by_class_name("sendbutton").click()
