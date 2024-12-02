import time
from cffi.cffi_opcode import CLASS_NAME
from select import select
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  Select
from parabank.login import login

driver=login()

def wait():
    time.sleep(2)

def login():
    user_name = "asdf"
    password = "pass"
    enter_username = driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[1]/input')
    enter_username.send_keys(user_name)
    enter_password = driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[2]/input')
    enter_password.send_keys(password)
    # time.sleep(3)
    click_login = driver.find_element(By.XPATH, '//*[@id="loginPanel"]/form/div[3]/input')
    click_login.click()
    wait()

def zoom_out():
    # action = ActionChains(driver)
    # action.key_down(Keys.CONTROL).send_keys(Keys.SUBTRACT).key_up(Keys.CONTROL).perform()
    driver.execute_script("document.body.style.zoom='50%'")

def scroll(n):
    for _ in range(n):  # Adjust the range for how many scrolls you want
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)  # Wait for a second between scrolls

def close_iframe():
    driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="q-messenger-frame"]'))
    close_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/span/div/div[1]/div/div/button')
    wait()
    close_button.click()
    driver.switch_to.default_content()
    zoom_out()
    # zoom_out()
    # driver.switch_to.frame(driver.find_element(By.XPATH, '// *[ @ id = "q-messenger-frame"]'))
    # close_iframe = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div[3]/button')
    # wait()
    # close_iframe.click()
    # driver.switch_to.default_content()
    # / html / body / iframe[2]
    # // *[ @ id = "q-messenger-frame"]
    # // *[ @ id = "ce_proto_iframe"]
    #
    # // *[ @ id = "q-messenger-frame"]
    # / html / body / div[1] / div / div / div[2] / div / div / div[1] / div / div[3] / button
    # zoom_out()

def open_solutions_page():
    click_product=driver.find_element(By.XPATH,'//*[@id="headerPanel"]/ul[1]/li[4]/a')
    click_product.click()
    # time.sleep(3)
    click_solutions = driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div/div/nav[1]/ul/li[2]/span')
    click_solutions.click()
    # time.sleep(3)
    click_learn_more = driver.find_element(By.XPATH, '/html/body/div[2]/header/div/div/div/nav[1]/ul/li[2]/div/div/div[1]/a')
    click_learn_more.click()
    # time.sleep(3)

def verify_solution_tabs():
    open_solutions_page()
    close_iframe()
    scroll(2)
    click_tab2 = driver.find_element(By.XPATH, '//*[@id="main"]/section[5]/div[2]/div[1]/ul/li[2]/button')
    click_tab2.click()
    click_tab3 = driver.find_element(By.XPATH, '//*[@id="main"]/section[5]/div[2]/div[1]/ul/li[3]/button')
    click_tab3.click()
    click_tab4 = driver.find_element(By.XPATH, '//*[@id="main"]/section[5]/div[2]/div[1]/ul/li[4]/button')
    click_tab4.click()
    click_tab1 = driver.find_element(By.XPATH, '//*[@id="main"]/section[5]/div[2]/div[1]/ul/li[1]/button')
    click_tab1.click()
    wait()

def request_a_demo():
    open_solutions_page()
    close_iframe()
    scroll(2)

    tab1_demo=driver.find_element(By.XPATH,'//*[@id="main"]/section[5]/div[2]/div[2]/div/div/div[1]/div[1]/div[1]/div/p[2]/a')
    tab1_demo.click()
    wait()
    driver.back()
    close_iframe()

    click_tab2 = driver.find_element(By.XPATH, '//*[@id="main"]/section[5]/div[2]/div[1]/ul/li[2]/button')
    click_tab2.click()
    tab2_demo = driver.find_element(By.XPATH,'//*[@id="main"]/section[5]/div[2]/div[2]/div/div/div[2]/div[1]/div[1]/div/p[2]/a')
    tab2_demo.click()
    wait()
    driver.back()
    close_iframe()

    click_tab3 = driver.find_element(By.XPATH, '//*[@id="main"]/section[5]/div[2]/div[1]/ul/li[3]/button')
    click_tab3.click()
    wait()
    tab3_demo = driver.find_element(By.XPATH,'//*[@id="main"]/section[5]/div[2]/div[2]/div/div/div[3]/div[1]/div[1]/div/p[2]/a')
    tab3_demo.click()
    wait()
    driver.back()
    close_iframe()

    click_tab4 = driver.find_element(By.XPATH, '//*[@id="main"]/section[5]/div[2]/div[1]/ul/li[4]/button')
    click_tab4.click()
    tab4_demo = driver.find_element(By.XPATH,'//*[@id="main"]/section[5]/div[2]/div[2]/div/div/div[4]/div[1]/div[1]/div/p[2]/a')
    tab4_demo.click()
    wait()
    driver.back()
    close_iframe()

    click_tab1 = driver.find_element(By.XPATH, '//*[@id="main"]/section[5]/div[2]/div[1]/ul/li[1]/button')
    click_tab1.click()
    wait()

def verify_industries_slider():
    open_solutions_page()
    close_iframe()
    scroll(4)
    click_slider2 = driver.find_element(By.XPATH, '//*[@id="main"]/section[6]/div[2]/div[2]/ul/li[2]/h2')
    click_slider2.click()
    click_slider3 = driver.find_element(By.XPATH, '//*[@id="main"]/section[6]/div[2]/div[2]/ul/li[3]/h2')
    click_slider3.click()
    click_slider4 = driver.find_element(By.XPATH, '//*[@id="main"]/section[6]/div[2]/div[2]/ul/li[4]/h2')
    click_slider4.click()
    click_slider5 = driver.find_element(By.XPATH, '//*[@id="main"]/section[6]/div[2]/div[2]/ul/li[5]/h2')
    click_slider5.click()
    click_slider6 = driver.find_element(By.XPATH, '//*[@id="main"]/section[6]/div[2]/div[2]/ul/li[6]/h2')
    click_slider6.click()
    click_slider7 = driver.find_element(By.XPATH, '//*[@id="main"]/section[6]/div[2]/div[2]/ul/li[7]/h2')
    click_slider7.click()
    click_slider8 = driver.find_element(By.XPATH, '//*[@id="main"]/section[6]/div[2]/div[2]/ul/li[8]/h2')
    click_slider8.click()
    click_slider1 = driver.find_element(By.XPATH, '//*[@id="main"]/section[6]/div[2]/div[2]/ul/li[1]/h2')
    click_slider1.click()
    wait()

def read_industries_slider():
    open_solutions_page()
    close_iframe()
    scroll(4)
    slider1_headtext = driver.find_element(By.XPATH, '//*[@id="i0"]/div[2]/div/h3').text
    print("Head:", slider1_headtext)
    slider1_paratext = driver.find_element(By.XPATH, '//*[@id="i0"]/div[2]/div/p[1]').text
    print("Para:", slider1_paratext)
    print()
    click_slider2 = driver.find_element(By.XPATH, '//*[@id="main"]/section[6]/div[2]/div[2]/ul/li[2]/h2')
    click_slider2.click()
    wait()
    slider2_headtext=driver.find_element(By.XPATH,'//*[@id="i1"]/div[2]/div/h3').text
    print("Head:",slider2_headtext)
    slider2_paratext=driver.find_element(By.XPATH,'//*[@id="i1"]/div[2]/div/p[1]').text
    print("Para:",slider2_paratext)
    print()
    click_slider3 = driver.find_element(By.XPATH, '//*[@id="main"]/section[6]/div[2]/div[2]/ul/li[3]/h2')
    click_slider3.click()
    wait()
    slider3_headtext = driver.find_element(By.XPATH, '//*[@id="i2"]/div[2]/div/h3').text
    print("Head:", slider3_headtext)
    slider3_paratext = driver.find_element(By.XPATH, '//*[@id="i2"]/div[2]/div/p[1]').text
    print("Para:", slider3_paratext)
    print()
    click_slider4 = driver.find_element(By.XPATH, '//*[@id="main"]/section[6]/div[2]/div[2]/ul/li[4]/h2')
    click_slider4.click()
    wait()
    wait()
    slider4_headtext = driver.find_element(By.XPATH, '//*[@id="i3"]/div[2]/div/h3').text
    print("Head:", slider4_headtext)
    slider4_paratext = driver.find_element(By.XPATH, '//*[@id="i3"]/div[2]/div/p[1]').text
    print("Para:", slider4_paratext)
    print()
    click_slider5 = driver.find_element(By.XPATH, '//*[@id="main"]/section[6]/div[2]/div[2]/ul/li[5]/h2')
    click_slider5.click()
    wait()
    wait()
    slider5_headtext = driver.find_element(By.XPATH, '//*[@id="i4"]/div[2]/div/h3').text
    print("Head:", slider5_headtext)
    slider5_paratext = driver.find_element(By.XPATH, '//*[@id="i4"]/div[2]/div/p[1]').text
    print("Para:", slider5_paratext)
    print()
    click_slider6 = driver.find_element(By.XPATH, '//*[@id="main"]/section[6]/div[2]/div[2]/ul/li[6]/h2')
    click_slider6.click()
    wait()
    wait()
    slider6_headtext = driver.find_element(By.XPATH, '//*[@id="i5"]/div[2]/div/h3').text
    print("Head:", slider6_headtext)
    slider6_paratext = driver.find_element(By.XPATH, '//*[@id="i5"]/div[2]/div/p[1]').text
    print("Para:", slider6_paratext)
    print()
    click_slider7 = driver.find_element(By.XPATH, '//*[@id="main"]/section[6]/div[2]/div[2]/ul/li[7]/h2')
    click_slider7.click()
    wait()
    wait()
    slider7_headtext = driver.find_element(By.XPATH, '//*[@id="i6"]/div[2]/div/h3').text
    print("Head:", slider7_headtext)
    slider7_paratext = driver.find_element(By.XPATH, '//*[@id="i6"]/div[2]/div/p[1]').text
    print("Para:", slider7_paratext)
    print()
    click_slider8 = driver.find_element(By.XPATH, '//*[@id="main"]/section[6]/div[2]/div[2]/ul/li[8]/h2')
    click_slider8.click()
    wait()
    wait()
    slider8_headtext = driver.find_element(By.XPATH, '//*[@id="i7"]/div[2]/div/h3').text
    print("Head:", slider8_headtext)
    slider8_paratext = driver.find_element(By.XPATH, '//*[@id="i7"]/div[2]/div/p[1]').text
    print("Para:", slider8_paratext)
    print()
    click_slider1 = driver.find_element(By.XPATH, '//*[@id="main"]/section[6]/div[2]/div[2]/ul/li[1]/h2')
    click_slider1.click()
    wait()

''' Note: Below there are 5 functions with each testcase functioning individually. To test them uncomment them individually'''

# open_solutions_page()
# verify_solution_tabs()
# request_a_demo()
# verify_industries_slider()
read_industries_slider()