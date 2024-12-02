import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def Driver():
    driver = webdriver.Chrome()
    return driver

driver = Driver()

class Register:
    def __init__(self, driver):
        self.driver = driver

    def fill_form(self):
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.execute_script("window.scrollTo(0, 700);")
        self.driver.find_element(By.ID, "customer.firstName").send_keys("xyz")
        self.driver.find_element(By.ID, "customer.lastName").send_keys("zyx")
        self.driver.find_element(By.ID, "customer.address.street").send_keys("abc")
        self.driver.find_element(By.ID, "customer.address.city").send_keys("def")
        self.driver.find_element(By.ID, "customer.address.state").send_keys("MP")
        self.driver.find_element(By.ID, "customer.address.zipCode").send_keys("123456")
        self.driver.find_element(By.ID, "customer.phoneNumber").send_keys("9876543212")
        self.driver.find_element(By.ID, "customer.ssn").send_keys("333444488")
        self.driver.find_element(By.ID, "customer.username").send_keys("tester1")
        self.driver.find_element(By.ID, "customer.password").send_keys("Tester@1")
        self.driver.find_element(By.ID, "repeatedPassword").send_keys("Tester@1")
        self.driver.find_element(By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input').click()
        time.sleep(4)

def login(driver):
    driver.find_element(By.NAME, "username").send_keys("tester1")
    driver.find_element(By.NAME, "password").send_keys("Tester@1")
    driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[3]/input').click()
    time.sleep(3)

# login()