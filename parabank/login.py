import time
from cffi.cffi_opcode import CLASS_NAME
from select import select
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  Select

def login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://parabank.parasoft.com/parabank/index.htm')
    user_name = "asdf"
    password = "pass"
    enter_username = driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[1]/input')
    enter_username.send_keys(user_name)
    enter_password = driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[2]/input')
    enter_password.send_keys(password)
    # time.sleep(3)
    click_login = driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[3]/input')
    click_login.click()
    # wait()
    time.sleep(3)
    return driver