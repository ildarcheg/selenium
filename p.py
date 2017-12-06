import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
from urllib.parse import quote

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
print("starting loop")

def get_next_page(base_url, soup):
	print("   looking for prev-next-pagelink")
	href_node = soup.find("a", { "class" : "prev-next-pagelink" })
	print(href_node)
	print("   getting href attribute")
	href= href_node['href']
	print("   href: "+href)
	return (base_url+href)



base_url = 'http://www.forum.mista.ru/'
temp = 'http://www.forum.mista.ru/topic.php?id=1'
temp = 'http://www.forum.mista.ru/topic.php?id=809323&page=2'
#temp = 'http://www.forum.mista.ru/topic.php?id=29'
for counter in range(1,30):
	url = base_url + 'topic.php?id=' + str(counter)
	print(url)
	driver.get(url)
	path = 'files/t-'+str(counter).zfill(7)+'-'+quote('url', safe='')
	new_file = open(path,'w')
	new_file.write(driver.page_source)

# wait = WebDriverWait(driver,10)
# wait.until(lambda driver: driver.find_element_by_id('under_messages'))
# html = driver.page_source
# path = 't1.html'
# new_file = open(path,'w')
# new_file.write(html)
# html = driver.page_source
# path = 't2.html'
# new_file = open(path,'w')
# new_file.write(html)
# html = driver.page_source
# path = 't3.html'
# new_file = open(path,'w')
# new_file.write(html)
# html = driver.page_source
# path = 't4.html'
# new_file = open(path,'w')
# new_file.write(html)
# html = driver.page_source
# path = 't5.html'
# new_file = open(path,'w')
# new_file.write(html)
# html = driver.page_source
# path = 't6.html'
# new_file = open(path,'w')
# new_file.write(html)
# html = driver.page_source
# path = 't7.html'
# new_file = open(path,'w')
# new_file.write(html)
# html = driver.page_source
# path = 't8.html'
# new_file = open(path,'w')
# new_file.write(html)
# html = driver.page_source
# path = 't9.html'
# new_file = open(path,'w')
# new_file.write(html)
# html = driver.page_source
# path = 't10.html'
# new_file = open(path,'w')
# new_file.write(html)
# for counter in range(1,30):
# 	url = base_url + 'topic.php?id=' + str(counter)
# 	print(url)
# 	print(" \n\n\n ")
# 	driver.get(url)
# 	html = driver.page_source
# 	print(html)
# 	print(" \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n ")

	# print("loading page: "+next_page_url)
	# driver.get(next_page_url)
	# wait = WebDriverWait(driver,10)
	# wait.until(lambda driver: driver.find_element_by_class_name("prev-next-pagelink"))
	# html = driver.page_source
	# soup = BeautifulSoup(html, "lxml")
	# next_page_url = get_next_page(base_url, soup)
	# print("   "+next_page_url)

#mya = soup.find("a", { "class" : "prev-next-pagelink" })
#print(mya)
#print(mya['href'])
#path = 't.html'
#new_file = open(path,'w')
#new_file.write(html)
