import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from urllib.parse import quote
from xvfbwrapper import Xvfb

vdisplay = Xvfb()
vdisplay.start()

def get_driver():
	url = "http://www.forum.mista.ru/index.php"
	driver = webdriver.Chrome()
	return driver

def authenticate(url, driver):
	driver.get(url)
	username = "Добрый хачик"
	password = "11"
	uname = driver.find_element_by_name("user_name")
	uname.send_keys(username)
	passw = driver.find_element_by_name("user_password")
	passw.send_keys(password)
	submit_button = driver.find_element_by_class_name("sendbutton").click()

base_url = 'http://www.forum.mista.ru/'
base_url_index = 'http://www.forum.mista.ru/index.php'

print("getting driver")
driver = get_driver()
print("logging")
authenticate(base_url, driver)
#print(driver.page_source.encode('windows-1251'))
d = driver.execute_script("return document.documentElement.outerHTML;").encode("utf-8")
print(d)
vdisplay.stop()
