import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#service_obj = Service("https://www.google.com/search?q=chrome+link&rlz=1C1GCHB_enIN1125IN1125&oq=Chrome+link&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBwgBEAAYgAQyBwgCEAAYgAQyBwgDEAAYgAQyBwgEEAAYgAQyBwgFEAAYgAQyBwgGEAAYgAQyBwgHEAAYgAQyBwgIEAAYgAQyBwgJEAAYgATSAQg4Nzk1ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8")
driver = webdriver.Chrome()  # invoke browser
driver.get("https://parabank.parasoft.com/parabank/admin.htm")
time.sleep(2)
driver.maximize_window()

# For Register
driver.find_element(By.XPATH,'//*[@id="loginPanel"]/p[2]/a').click()
time.sleep(2)
# For username
driver.find_element(By.XPATH,'//*[@id="customer.firstName"]').send_keys('Minni')
# Lastname
driver.find_element(By.XPATH,'//*[@id="customer.lastName"]').send_keys('kumari')
driver.find_element(By.XPATH,'//*[@id="customer.address.street"]').send_keys('global village')
driver.find_element(By.XPATH,'//*[@id="customer.address.city"]').send_keys('banglore')
driver.find_element(By.XPATH,'//*[@id="customer.address.state"]').send_keys('karnataka')
driver.find_element(By.XPATH,'//*[@id="customer.address.zipCode"]').send_keys('56059')
driver.find_element(By.XPATH,'//*[@id="customer.phoneNumber"]').send_keys('1234567890')
driver.find_element(By.XPATH,'//*[@id="customer.ssn"]').send_keys('123')
time.sleep(1)
# Username
driver.find_element(By.XPATH,'//*[@id="customer.username"]').send_keys('miniikumari')
driver.find_element(By.XPATH,'//*[@id="customer.password"]').send_keys('mini@123')
driver.find_element(By.XPATH,'//*[@id="repeatedPassword"]').send_keys('mini@123')
driver.find_element(By.XPATH,'//*[@id="customerForm"]/table/tbody/tr[13]/td[2]/input').click()
time.sleep(2)

# product
driver.find_element(By.XPATH,'//*[@id="headerPanel"]/ul[1]/li[4]/a').click()
time.sleep(3)
# remove chat
driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="q-messenger-frame"]'))
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/span/div/div[1]/div/div/button").click()
time.sleep(3)
driver.switch_to.default_content()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[2]/header/div/div/div/nav[1]/ul/li[1]/span').click()
time.sleep(3)

driver.execute_script("document.body.style.zoom='50%'")
time.sleep(3)
# For selenic
driver.find_element(By.XPATH,'/html/body/div[2]/header/div/div/div/nav[1]/ul/li[1]/div/div/div[2]/ul/li[8]/a/span[2]').click()
time.sleep(5)

# for Zoom out
driver.execute_script("document.body.style.zoom='50%'")
time.sleep(3)
# overview option
driver.find_element(By.XPATH,'//*[@id="main"]/section[3]/div/div/div/div[2]/nav/ul/li[1]/a').click()
time.sleep(4)
# For scroll
driver.execute_script("window.scrollTo(0,900);")
time.sleep(3)
# For Learn more
driver.find_element(By.XPATH,'//*[@id="capabilities"]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/p[3]/a[2]').click()
time.sleep(4)
# Start free trial
driver.find_element(By.XPATH,'//*[@id="main"]/section[5]/div[2]/div[3]/a[1]').click()
time.sleep(4)
# fill email id, name , last name, cmpany name...etc.
driver.find_element(By.XPATH,'//*[@id="email-c99fe155-37de-4548-8c0b-048d5aec6eac"]').send_keys('m.kumari@gmail.com')
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="firstname-c99fe155-37de-4548-8c0b-048d5aec6eac"]').send_keys('Minni')
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="lastname-c99fe155-37de-4548-8c0b-048d5aec6eac"]').send_keys('kumari')
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="company-c99fe155-37de-4548-8c0b-048d5aec6eac"]').send_keys('CG')
time.sleep(4)
driver.find_element(By.XPATH,'//*[@id="jobtitle-c99fe155-37de-4548-8c0b-048d5aec6eac"]').send_keys('software Testing')
time.sleep(4)
# For country
driver.find_element(By.XPATH,'//*[@id="country-c99fe155-37de-4548-8c0b-048d5aec6eac"]').send_keys('India')
time.sleep(4)
for country in countries:
    if country.text=="India":
     country.click()
     break

# get started button
driver.find_element(By.XPATH,'//*[@id="hsForm_c99fe155-37de-4548-8c0b-048d5aec6eac"]/div/div[2]/input').click()
time.sleep(4)
driver.execute_script("window.scrollTo(0,900);")
time.sleep(3)



