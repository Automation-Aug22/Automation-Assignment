import time

from selenium.webdriver.common.by import By

from BhavanaPractice.Parabank.Parabank2.Usercredential import firstName, lastName, street, city, state, zipcode, \
    phonenumber, username, ssn, password, reenter

# def login(driver):
#     time.sleep(2)
#     driver.find_element(By.XPATH,'//*[@id="loginPanel"]/form/div[1]/input').send_keys("BhavanaMH")
#     time.sleep(1)
#     driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[2]/input').send_keys("BhavanaMH123")
#     time.sleep(1)
#     driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[3]/input').click()
#     time.sleep(2)

def register_page(driver):
    driver.find_element(By.XPATH, '//*[@id="loginPanel"]/p[2]/a').click()
    time.sleep(2)

    #Enter name
    driver.find_element(By.XPATH, '//*[@id="customer.firstName"]').send_keys("BhavanaH")
    time.sleep(1)

    #Enter the last name
    driver.find_element(By.XPATH, '//*[@id="customer.lastName"]').send_keys("Harikant")
    time.sleep(1)

    #Enter the address
    driver.find_element(By.XPATH, '//*[@id="customer.address.street"]').send_keys("Btm Layout")
    time.sleep(1)

    #Enter the city
    driver.find_element(By.XPATH, '//*[@id="customer.address.city"]').send_keys("Bengaluru")
    time.sleep(1)

    #Enter the state
    driver.find_element(By.XPATH, "//input[@id='customer.address.state']").send_keys("Karnataka")
    time.sleep(1)

    #Enter the zipcode
    driver.find_element(By.XPATH, '//*[@id="customer.address.zipCode"]').send_keys("123456")
    time.sleep(1)

    #Enter the phone number
    driver.find_element(By.XPATH, '//*[@id="customer.phoneNumber"]').send_keys("9563425783")
    time.sleep(1)

    #Enter the ssn
    driver.find_element(By.XPATH, '//*[@id="customer.ssn"]').send_keys("87699")
    time.sleep(1)

    #Enter the username
    driver.find_element(By.XPATH, '//*[@id="customer.username"]').send_keys("BhavanaMH")
    time.sleep(1)

    #Enter the password
    driver.find_element(By.XPATH, '//*[@id="customer.password"]').send_keys("BhavanaMH123")
    time.sleep(1)

    #Rewrite the password
    driver.find_element(By.XPATH, '//*[@id="repeatedPassword"]').send_keys("BhavanaMH123")
    time.sleep(1)

    #Click on register
    driver.find_element(By.XPATH, '//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input').click()
    time.sleep(5)

    # try:
    #     text=driver.find_element(By.XPATH,'//*[@id="rightPanel"]/p').text()
    #     if "If you have an account with us you can sign-up for free instant" in text:
    #         login(driver)
    #     else:
    #         print(text)
    # except:
    #     print("Error occured while checking the login information 1")


def register_main(driver):
    driver.get('https://parabank.parasoft.com/parabank/index.htm')
    driver.maximize_window()
    time.sleep(2)

    #Click on register
    register_page(driver)
