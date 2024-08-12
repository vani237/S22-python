#tiin one stage of the pipeline , we need to check if jfrog server is up and can accept credentials.
#Any artifact push. please write a python script to do this.cket: 

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
#time.sleep(2)
driver.maximize_window()
#time.sleep(2)
driver.get("http://54.197.99.224:8080")

username = driver.find_element(by=By.NAME, value='j_username')
password = driver.find_element(by=By.NAME, value='j_password')
username.send_keys('devops')
password.send_keys('devops')
submit_button = driver.find_element(by=By.NAME, value='Submit')
submit_button.click()
time.sleep(4)