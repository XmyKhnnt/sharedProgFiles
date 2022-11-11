


import os
from selenium import webdriver
from selenium.webdriver.common.by import By




os.environ['PATH'] +=  r'D:\ProgrammingProject\chromedriver.exe'
driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
driver.implicitly_wait(10)



def login(em, pss):
    email = driver.find_element(By.ID, 'email')
    password = driver.find_element(By.ID, 'pass')
    login = driver.find_element(By.CSS_SELECTOR, 'button[name="login"]')

    email.send_keys(em)
    password.send_keys(pss)
    login.click()


login("Khent", 'IamHandsome')