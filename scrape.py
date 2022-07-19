from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'creds.env')
load_dotenv(dotenv_path)

LOGIN = os.environ.get("LOGIN")
PASS = os.environ.get("PASS")
DEPT = os.environ.get("DEPT")
CLASS = os.environ.get("CLASS")
DRIVER_LOC = os.environ.get("DRIVER_LOC")

driver = webdriver.Chrome(DRIVER_LOC)

driver.get("https://be.my.ucla.edu/ClassPlanner/ClassPlan.aspx")
fillUser = driver.find_element(By.XPATH, '//*[@id="logon"]')
fillUser.click()
fillUser.send_keys(LOGIN)

fillPass = driver.find_element(By.XPATH, '//*[@id="pass"]')
fillPass.click()
fillPass.send_keys(PASS)

driver.find_element(By.XPATH,'//*[@id="sso"]/form/div/table/tbody/tr/td[1]/button').click()

def finchecker():
    try: 
        check = False
        check = driver.find_element(By.XPATH,'//*[@id="titleText"]')
        print(check)
        return check
    except:
        time.sleep(1)
while(not finchecker()):
    print('Not in yet')

print("WE'RE IN")
driver.get("https://be.my.ucla.edu/ClassPlanner/ClassPlan.aspx")


fillDept = driver.find_element(By.XPATH, '//*[@id="searchTier0"]')
fillDept.click()
fillDept.send_keys(DEPT)
time.sleep(2)
fillDept.send_keys(Keys.RETURN)

time.sleep(2)

fillClass = driver.find_element(By.XPATH, '//*[@id="searchTier1"]')
fillClass.click()
fillClass.send_keys(CLASS)
time.sleep(1)
fillClass.send_keys(Keys.RETURN)

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="ctl00_MainContent_cs_goButton"]').click()

while(True):
    time.sleep(5)
    e = driver.find_element(By.XPATH, '//*[@id="data_course_M0_187510200"]/div[3]')
    print(e.text)
    driver.find_element(By.XPATH, '//*[@id="ctl00_MainContent_cs_goButton"]').click()
    pass