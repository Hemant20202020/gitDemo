import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(r"C:\Users\hp\Downloads\chromedriver_win32 (1)\chromedriver.exe")

driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
driver.implicitly_wait(5)
action=ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,'mousehover')).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,'Top')).perform()
time.sleep(1)
action.move_to_element(driver.find_element(By.LINK_TEXT,'Reload')).click().perform()

