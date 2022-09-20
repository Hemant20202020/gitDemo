import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
chrome_opt=webdriver.ChromeeOptions()
chrome_opt.add_argument('--start-maximized')
driver=webdriver.Chrome(r"C:\Users\hp\Downloads\chromedriver_win32 (1)\chromedriver.exe",options=chrome_opt)
driver.implicitly_wait(5)
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.find_element(By.XPATH,"//a[text()='Shop']").click()
products=driver.find_elements(By.XPATH,"//div[@class='card h-100']")
for prod in products:
    prodcutName=prod.find_element(By.XPATH,"div/h4/a").text
    if prodcutName=='Blackberry':
        prod.find_element(By.XPATH,'div/button').click()

driver.find_element(By.XPATH,"//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.CSS_SELECTOR,"button[class*='btn-success']").click()
driver.find_element(By.ID,'country').send_keys('ind')
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,'India')))
driver.find_element(By.LINK_TEXT,'India').click()
driver.find_element(By.CSS_SELECTOR,'div[class*="checkbox-primary"]').click()
driver.find_element(By.CSS_SELECTOR,"input[class*='btn-success']").click()
print(driver.find_element(By.CSS_SELECTOR,"div[class*='alert-success']").text)

driver.quit()