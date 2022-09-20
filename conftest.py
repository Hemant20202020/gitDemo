import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope='class')
def setup(request):
    chrome_opt = webdriver.ChromeOptions()
    chrome_opt.add_argument('--start-maximized')
    driver = webdriver.Chrome(r"C:\Users\hp\Downloads\chromedriver_win32 (1)\chromedriver.exe", options=chrome_opt)
    driver.implicitly_wait(5)
    driver.get('https://rahulshettyacademy.com/angularpractice/')
    request.cls.driver=driver
    yield
    driver.close()