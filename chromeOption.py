import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

chrome_opt=webdriver.ChromeOptions()
chrome_opt.add_argument('headless')
chrome_opt.add_argument('--start-maximized')
chrome_opt.add_argument('--ignore-certificate-errors')
driver=webdriver.Chrome(r"C:\Users\hp\Downloads\chromedriver_win32 (1)\chromedriver.exe",options=chrome_opt)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/offers')
print(driver.title)
