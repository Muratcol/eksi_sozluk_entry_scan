from selenium import webdriver
import re
import time


entries = []
browser = webdriver.Firefox()

b_url = "https://eksisozluk.com/en-iyi-ayran-markasi--3810169?p="
for i in range(1,2):
	url = b_url + str(i)
	browser.get(url)
	elements = browser.find_elements_by_css_selector('.content')
	for element in elements:
		cleanString = re.sub('[.|,|:|;]',' ', element.text )
		entries.append(cleanString)
	time.sleep(3)


with open("C:/Users/Murat/Desktop/Python Çalışmaları/Selenium_Data_Analyses/selenium_eksi/ayranlar.txt", 'w+', encoding = "UTF-8") as f:
	for entry in entries:
		f.write(entry + ",")


browser.close()