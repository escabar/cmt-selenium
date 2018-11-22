#!/usr/bin/python3

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def init_driver():
    driver = webdriver.Chrome()
    driver.get('https://wm.automanager.com/login.aspx')
    driver.implicitly_wait(2)
    return driver


def login_to_wm():
    driver.find_element(by=By.ID, value='ctl00_cphMain_txtClientID').send_keys('')
    driver.find_element(by=By.ID, value='ctl00_cphMain_txtUsername').send_keys('')
    driver.find_element(by=By.ID, value='ctl00_cphMain_txtPassword').send_keys('')
    driver.find_element(by=By.ID, value='btnLogin').click()
    driver.implicitly_wait(2)
    #driver.find_element(by=By.ID, value='ui-id-1').send_keys(Keys.ENTER)
    #driver.find_element(by=By.XPATH, value='//').send_keys(Keys.ENTER)
    #driver.find_element(by=By.XPATH, value='//*[contains(text(),"OK")]').send_keys(Keys.ENTER)

def update_carfax():
    driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Settings').click()
    driver.find_element(by=By.PARTIAL_LINK_TEXT, value='buyers guides').click()
    driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Vehicle History Reports').click()
    driver.find_element(by=By.XPATH, value='//button[contains(text(),"Upgraded Reports")]').click()
    # driver.find_element(by=By.XPATH, value='//button[contains(text(),"Log Out")]').click()
    # driver.find_element(by=By.XPATH, value='//button[contains(text(),"Close")]').click()


def tear_down():
    driver.quit()


if __name__ == "__main__":
    driver = init_driver()
    login_to_wm()
    time.sleep(2)
    update_carfax()
    tear_down()
