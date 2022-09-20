import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(r"C:\Users\hp\Downloads\chromedriver_win32 (1)\chromedriver.exe")
driver.get('https://the-internet.herokuapp.com/iframe')
driver.implicitly_wait(2)
driver.switch_to.frame('mce_0_ifr')
driver.find_element(By.ID,'tinymce').clear()
driver.find_element(By.ID,'tinymce').send_keys('i am richest person on the earth.')
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME,'h3').text)
