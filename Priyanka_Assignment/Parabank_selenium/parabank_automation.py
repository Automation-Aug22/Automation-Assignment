import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
#To visit the para bank website
driver.get("https://parabank.parasoft.com/parabank/index.htm")
driver.maximize_window()
#To Log in the website
driver.find_element(By.NAME,"username").send_keys("Priya")
driver.find_element(By.NAME,"password").send_keys("Priya@123")
driver.find_element(By.XPATH,'//*[@id="loginPanel"]/form/div[3]/input').click()
#To visit the product site
driver.find_element(By.XPATH,'//*[@id="headerPanel"]/ul[1]/li[4]/a').click()
#To choose industries option from product
driver.find_element(By.XPATH,'/html/body/div[2]/header/div/div/div/nav[1]/ul/li[3]/span').click()
#To choose automotive
driver.find_element(By.XPATH,"//div[@class='menu']//a[normalize-space()='Automotive']").click()
#To read the case study
driver.find_element(By.XPATH,"//a[normalize-space()='Read Case Study']").click()
#To go to the same page where explore and read case study was there
driver.get("https://www.parasoft.com/industries/embedded/automotive/")

#To choose explore products from automotive
driver.find_element(By.XPATH,"//a[normalize-space()='Explore Products']").click()
time.sleep(3)

#To go to filter and solution options
checkboxes = driver.find_elements(By.CSS_SELECTOR, "li[class='sf-field-taxonomy-solutions'] h4")  # Replace with actual selector


driver.find_element(By.XPATH,"//li[@class='sf-field-taxonomy-solutions']//h4[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//label[@for='sf-input-fb873c63d3fa2547d2aa73a43b544890']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//li[@class='sf-field-taxonomy-solutions']//h4[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//li[@class='sf-field-taxonomy-industry']//h4[1]").click()
time.sleep(2)
driver.find_element(By.XPATH,"//h4[@class='active']").click()
time.sleep(2)
driver.find_element(By.NAME,"_sf_submit").click()
time.sleep(2)
driver.find_element(By.XPATH,"//h4[normalize-space()='C/C++test']").click()
time.sleep(4)
driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='q-messenger-frame']"))
driver.find_element(By.XPATH,"//*[name()='use' and contains(@href,'#timesIcon')]").click()
time.sleep(5)
driver.switch_to.default_content()
time.sleep(2)
driver.execute_script("document.body.style.zoom='25%'")
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="main"]/section[3]/div/div/div/div[3]/a').click()
time.sleep(2)
driver.execute_script("window.scrollTo(0, 900);")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@id='email-ac031725-1541-4bcb-a4b1-baf748fba09b']").send_keys("hello@intel.com")
driver.find_element(By.XPATH,"//input[@id='firstname-ac031725-1541-4bcb-a4b1-baf748fba09b']").send_keys("Priyanka")
driver.find_element(By.XPATH,"//input[@id='lastname-ac031725-1541-4bcb-a4b1-baf748fba09b']").send_keys("Singh")
driver.find_element(By.XPATH,"//input[@id='company-ac031725-1541-4bcb-a4b1-baf748fba09b']").send_keys("intel")
driver.find_element(By.XPATH,"//input[@id='jobtitle-ac031725-1541-4bcb-a4b1-baf748fba09b']").send_keys("engineer")
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='phone-ac031725-1541-4bcb-a4b1-baf748fba09b']").send_keys("6202409232")
time.sleep(2)
driver.find_element(By.XPATH,"//select[@id='country-ac031725-1541-4bcb-a4b1-baf748fba09b']").send_keys("ind")
countries = driver.find_elements(By.XPATH,"//select[@id='country-ac031725-1541-4bcb-a4b1-baf748fba09b']/option")
for country in countries:
    if country.text == "India":
        country.click()
        break
time.sleep(3)
driver.execute_script("document.body.style.zoom='80%'")
time.sleep(5)
driver.find_element(By.XPATH,"//input[@value='REQUEST DEMO']").click()
time.sleep(3)










