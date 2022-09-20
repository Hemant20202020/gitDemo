import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from BaseClass import BaseClass


class TestClass(BaseClass):
    def test_e2e(self):


        self.driver.find_element(By.XPATH, "//a[text()='Shop']").click()
        products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for prod in products:
            prodcutName = prod.find_element(By.XPATH, "div/h4/a").text
            if prodcutName == 'Blackberry':
                prod.find_element(By.XPATH, 'div/button').click()

        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()
        self.driver.find_element(By.ID, 'country').send_keys('ind')
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
        self.driver.find_element(By.LINK_TEXT, 'India').click()
        self.driver.find_element(By.CSS_SELECTOR, 'div[class*="checkbox-primary"]').click()
        self.driver.find_element(By.CSS_SELECTOR, "input[class*='btn-success']").click()
        print(self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text)
