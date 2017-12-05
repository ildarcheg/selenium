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