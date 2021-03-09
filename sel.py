from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Firefox()
driver.get('http://www.google.com')

elem = driver.find_element_by_name("q")
elem.send_keys('do a test search' + Keys.RETURN)