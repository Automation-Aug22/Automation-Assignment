import time
from selenium.webdriver.support.select import Select
from AdminPage import Driver
from AdminPage import login
from selenium.webdriver.common.by import By

class Parasoft:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def open_parasoft(self):
        self.driver.get("https://parabank.parasoft.com/parabank/admin.htm")
        self.driver.maximize_window()
        time.sleep(2)


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
        time.sleep(2)

class Products:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_products(self):
        self.driver.find_element(By.LINK_TEXT, "Products").click()
        time.sleep(5)
        self.driver.find_element(By.LINK_TEXT, "Get Started").click()
        time.sleep(2)


class Chat:
    def __init__(self, driver):
        self.driver = driver

    def open_chat(self):
        self.driver.find_element(By.LINK_TEXT, "Chat Now").click()
        time.sleep(3)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, '//*[@id="q-messenger-frame"]'))
        close = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[3]/button')
        close.click()
        self.driver.switch_to.default_content()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1300);")
        time.sleep(2)


class FreeTrial:
    def __init__(self, driver):
        self.driver = driver

    def apply_for_free_trial(self):
        self.driver.execute_script("document.body.style.zoom='35%'")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//body/div[@class='b-page']/main[@id='main']/section[@class='TRY-PARASOFT']/div[@class='b-frame']/div[@class='b-columns alt-loose']/div[@class='b-column']/div[@id='results']/div[@class='b-columns']/div[8]/div[1]/div[2]/a[1]").click()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 400);")
        time.sleep(3)


class SeleniumTesting:
    def __init__(self, driver):
        self.driver = driver

    def perform_testing(self):
        self.driver.find_element(By.ID, 'email-c99fe155-37de-4548-8c0b-048d5aec6eac').send_keys("test1@capg.com")
        self.driver.find_element(By.ID, 'firstname-c99fe155-37de-4548-8c0b-048d5aec6eac').send_keys("test1")
        self.driver.find_element(By.ID, 'lastname-c99fe155-37de-4548-8c0b-048d5aec6eac').send_keys("xyz")
        self.driver.find_element(By.ID, 'company-c99fe155-37de-4548-8c0b-048d5aec6eac').send_keys("CapG")
        self.driver.find_element(By.ID, 'jobtitle-c99fe155-37de-4548-8c0b-048d5aec6eac').send_keys("Tester")
        self.driver.find_element(By.ID, 'phone-c99fe155-37de-4548-8c0b-048d5aec6eac').send_keys("9876543212")
        self.driver.execute_script("window.scrollTo(0, 600);")
        dropdown = Select(self.driver.find_element(By.ID, 'country-c99fe155-37de-4548-8c0b-048d5aec6eac'))
        dropdown.select_by_value("India")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="hsForm_c99fe155-37de-4548-8c0b-048d5aec6eac"]/div/div[2]/input').click()
        time.sleep(5)


# Main Execution
if __name__ == "__main__":
    driver = Driver()
    driver.implicitly_wait(5)

    # Create objects of each class
    parasoft = Parasoft(driver)
    register = Register(driver)
    products = Products(driver)
    chat = Chat(driver)
    free_trial = FreeTrial(driver)
    selenium_testing = SeleniumTesting(driver)

    # Execute methods using objects
    parasoft.open_parasoft()
    login(driver)
    # register.fill_form()
    products.navigate_to_products()
    chat.open_chat()
    free_trial.apply_for_free_trial()
    selenium_testing.perform_testing()
