from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'creds.env')
load_dotenv(dotenv_path)

USER = os.environ.get("USER")
PASS = os.environ.get("PASS")

PATH = r"C:\Users\Alan\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)


driver.get("https://be.my.ucla.edu/ClassPlanner/ClassPlan.aspx")
fill = driver.find_element(By.XPATH, '//*[@id="logon"]')
fill.click()
fill.send_keys(USER)

fill = driver.find_element(By.XPATH, '//*[@id="pass"]')
fill.click()
fill.send_keys(PASS)

driver.find_element(By.XPATH,'//*[@id="sso"]/form/div/table/tbody/tr/td[1]/button').click()

while(True):
    pass