import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://parabank.parasoft.com/parabank/admin.htm")
driver.maximize_window()
time.sleep(2)

class AutomationTest:
    def __init__(self):
        self.driver = webdriver.Chrome()

if __name__ == "__Automation__":
    test = AutomationTest()


def register():
        driver.find_element(By.LINK_TEXT, "Register").click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="customer.firstName"]').send_keys("qwerty")
        driver.find_element(By.XPATH, '//*[@id="customer.lastName"]').send_keys("poiu")
        driver.find_element(By.XPATH, '//*[@id="customer.address.street"]').send_keys("lane 1")
        driver.find_element(By.XPATH, '//*[@id="customer.address.city"]').send_keys("srinagar")
        driver.find_element(By.XPATH, '//*[@id="customer.address.state"]').send_keys("Jammu")
        driver.find_element(By.XPATH, '//*[@id="customer.address.zipCode"]').send_keys("1123456")
        driver.find_element(By.XPATH, '//*[@id="customer.phoneNumber"]').send_keys("1234567890")
        driver.find_element(By.XPATH, '//*[@id="customer.ssn"]').send_keys("0987")
        driver.find_element(By.XPATH, '//*[@id="customer.username"]').send_keys("qwerty")
        driver.find_element(By.XPATH, '//*[@id="customer.password"]').send_keys("1234")
        driver.find_element(By.XPATH, '//*[@id="repeatedPassword"]').send_keys("1234")
        driver.find_element(By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input').click()

def customer_login():
    driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[1]/input').send_keys("qwerty")
    driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[2]/input').send_keys("1234")
    driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[3]/input').click()

def location():
    driver.find_element(By.XPATH, '//*[@id="headerPanel"]/ul[1]/li[5]/a').click()
    driver.execute_script("window.scrollTo(0, 1200);")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="main"]/section[5]/div[2]/div[1]/ul/li[2]/button').click()
    driver.execute_script("window.scrollTo(0, 1700);")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="main"]/section[5]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/a').click()

register()
customer_login()
location()



