import time
from selenium.webdriver.common.by import By
from Sharanya_Parabank.utilities.BaseClass import BaseClass

firstName = "Sharanya"
lastName = "Biradar"
street = "Vasundhara Nagar Colony"
city = "Zaheerabad"
state = "Telangana"
zipCode = "502220"
phoneNumber = "8919651251"
ssn = "555-77-8888"

username = "Sharanya"
password = "shakti123"


class TestOne(BaseClass):

    def test_01(self):
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "customer.firstName").send_keys(firstName)
        self.driver.find_element(By.ID, "customer.lastName").send_keys(lastName)
        self.driver.find_element(By.ID, "customer.address.street").send_keys(street)
        self.driver.find_element(By.ID, "customer.address.city").send_keys(city)
        self.driver.find_element(By.ID, "customer.address.state").send_keys(state)
        self.driver.find_element(By.ID, "customer.address.zipCode").send_keys(zipCode)
        self.driver.find_element(By.ID, "customer.phoneNumber").send_keys(phoneNumber)
        self.driver.find_element(By.ID, "customer.ssn").send_keys(ssn)


    def test_02(self):
        self.driver.find_element(By.ID, "customer.username").send_keys(username)
        self.driver.find_element(By.ID, "customer.password").send_keys(password)
        self.driver.find_element(By.ID, "repeatedPassword").send_keys(password)
        self.driver.find_element(By.XPATH, "//input[@value='Register']").click()

    def test_03(self):
        self.driver.find_element(By.LINK_TEXT,"Admin Page").click()
        titletext = self.driver.find_element(By.XPATH,"//h1[@class='title']").text
        assert titletext == "Administration"

    def test_04(self):
        self.driver.find_element(By.XPATH,"//button[@value='INIT']").click()
        inittext = self.driver.find_element(By.XPATH,"//*[text()='Database Initialized']").text
        assert inittext == "Database Initialized"


    def test_05(self):
        self.driver.find_element(By.XPATH, "//button[@value='CLEAN']").click()
        cleantext = self.driver.find_element(By.XPATH, "//*[text()='Database Cleaned']").text
        assert cleantext == "Database Cleaned"






