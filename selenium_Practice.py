import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome(r"C:\Users\hp\Downloads\chromedriver_win32 (1)\chromedriver.exe")
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.CSS_SELECTOR,'.search-keyword').send_keys('ber')
time.sleep(2)
slt=driver.find_elements(By.CSS_SELECTOR,"div[class='product'] button")

print(len(slt))
for item in slt:
    item.click()

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
prices=driver.find_elements(By.XPATH,'//td[5]/p')
sum=0
for price in prices:
    sum=sum+int(price.text)

print('sum :',sum)
total=driver.find_element(By.CSS_SELECTOR,'.totAmt').text
assert sum==int(total)
driver.find_element(By.CSS_SELECTOR,'.promoCode').send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR,'.promoBtn').click()
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,'.promoInfo')))
print(driver.find_element(By.CSS_SELECTOR,'.promoInfo').text)

driver.close()