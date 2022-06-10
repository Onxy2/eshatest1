import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

options = webdriver.ChromeOptions()

#driver = webdriver.Chrome(options=options)


driver.get('https://esha.com/')
title = driver.title 
print(driver.title)
assert title == "Hire Ken"
driver.quit()    


