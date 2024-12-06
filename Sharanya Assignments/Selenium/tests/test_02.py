import time
from selenium.webdriver.common.by import By
from Sharanya_Parabank.utilities.BaseClass import BaseClass

class TestTwo(BaseClass):

    def test_06(self):
        self.driver.find_element(By.LINK_TEXT, "Locations").click()
        self.driver.find_element(By.XPATH, "//span[@class='link'][text()='Industries ']").click()
        self.driver.find_element(By.XPATH, "//div[@class='menu']//a[normalize-space()='Industrial Automation']").click()


    def test_07(self):
        self.driver.find_element(By.LINK_TEXT, "Explore Products").click()
        self.driver.execute_script("window.scrollTo(0, 500);")
        time.sleep(5)

        self.driver.find_element(By.XPATH, "//h4[normalize-space()='Solutions']").click()
        check_box = self.driver.find_element(By.XPATH, "//label[@for='sf-input-931d55a248d26480d074cf5b3a27a726']")
        check_box.click()
        self.driver.find_element(By.XPATH, "//h4[@class='active']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Search']").click()


    def test_08(self):
        self.driver.execute_script("window.scrollTo(0, 1500);")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//div[7]//div[1]//div[2]//button[1]").click()
        title_text = self.driver.find_element(By.XPATH,
                                              "//div[@class='b-modal-content']//h4[contains(text(),'Parasoft SOAtest')]").text
        print(title_text)
        content_text = self.driver.find_element(By.XPATH,
                                                "//div[@class='b-modal-content']//p[contains(text(),'Simplify')]").text
        print(content_text)
        time.sleep(5)
