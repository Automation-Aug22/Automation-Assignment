import time

from selenium import webdriver
from Registerpage import register_main
from Testcaseforsolutionpage import testcase_main


def main():
    driver=webdriver.Chrome()
    driver.get('https://parabank.parasoft.com/parabank/index.htm')
    driver.maximize_window()
    time.sleep(2)
    register_main(driver)
    time.sleep(2)
    testcase_main(driver)
    time.sleep(2)

if __name__=="__main__":
    main()