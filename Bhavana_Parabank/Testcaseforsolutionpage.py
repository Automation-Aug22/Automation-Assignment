import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def tc1(driver):
    #Clickng the product page to view whether the product page loaded properly or not
    driver.find_element(By.XPATH, '//*[@id="headerPanel"]/ul[1]/li[4]/a').click()


def tc2(driver):
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='q-messenger-frame']"))
    driver.find_element(By.XPATH,"//*[name()='use' and contains(@href,'#timesIcon')]").click()
    time.sleep(5)
    driver.switch_to.default_content()

def tc3(driver):
    driver.find_element(By.XPATH,"//span[@class='link'][normalize-space()='Solutions']").click()
    time.sleep(2)

def tc4(driver):
    driver.find_element(By.XPATH,"//div[@class='menu']//a[normalize-space()='AI & ML']").click()
    time.sleep(2)

    out=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="main"]/section[2]/div[2]/div/div/div/h1')))
    print(out.text)

def tc5(driver):

    driver.execute_script("document.body.style.zoom='25%'")
    time.sleep(5)

    out = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
        (By.XPATH,'//*[@id="main"]/section[4]/div[2]/div[1]/p[2]/strong/a')))
    out.click()

    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)

def tc6(driver):
    driver.execute_script("window.scrollBy(0, -1000);")
    time.sleep(2)

    driver.execute_script("document.body.style.zoom='25%'")
    time.sleep(5)

    dropdown=driver.find_element(By.XPATH,"//select[@aria-label='Select Language']")

    select = Select(dropdown)

    select.select_by_index(3)

def testcase_main(driver):

    driver.maximize_window()

    tc1(driver)
    time.sleep(5)

    tc2(driver)
    time.sleep(5)
    tc3(driver)
    time.sleep(5)
    tc4(driver)
    time.sleep(5)
    tc5(driver)
    time.sleep(5)
    tc6(driver)
    time.sleep(5)
