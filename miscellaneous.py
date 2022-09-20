import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

ListItem=[]
driver=webdriver.Chrome(r"C:\Users\hp\Downloads\chromedriver_win32 (1)\chromedriver.exe")
driver.maximize_window()
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')

driver.find_element(By.XPATH,'//span[text()="Veg/fruit name"]').click()
veggieList=driver.find_elements(By.XPATH,"//tr/td[1]")
for item in veggieList:
    ListItem.append(item.text)

original_list=ListItem.copy()
ListItem.sort()
assert original_list==ListItem

time.sleep(1)
driver.close()

