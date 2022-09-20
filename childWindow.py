import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(r"C:\Users\hp\Downloads\chromedriver_win32 (1)\chromedriver.exe")
driver.get('https://the-internet.herokuapp.com/windows')
driver.implicitly_wait(2)
driver.find_element(By.LINK_TEXT,'Click Here').click()
windowsName=driver.window_handles
driver.switch_to.window(windowsName[1])
print(driver.find_element(By.TAG_NAME,'h3').text)
driver.close()
driver.switch_to.window(windowsName[0])
print(driver.find_element(By.TAG_NAME,'h3').text)





time.sleep(1)
driver.quit()