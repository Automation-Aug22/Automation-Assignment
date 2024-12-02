import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def Driver():
    driver = webdriver.Chrome()
    return driver

driver = Driver()

def login(driver):
    driver.find_element(By.NAME, "username").send_keys("tester1")
    driver.find_element(By.NAME, "password").send_keys("Tester@1")
    driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[3]/input').click()
    time.sleep(3)

# login()