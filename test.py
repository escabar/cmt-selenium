'''

from selenium import webdriver
from selenium.webdriver.common.by import By

import time


driver = webdriver.Chrome()
driver.get('https://wm.automanager.com/login.aspx')
driver.implicitly_wait(2)

try:

    username = browser.find_element(by=By.ID, value='login-email').send_keys('solly.p@gmail.com')
    password = browser.find_element(by=By.ID, value='login-password').send_keys('basis100!')
    login = browser.find_element(by=By.ID, value='login-submit').click()


    driver.find_element(by=By.ID, value='ctl00_cphMain_txtClientID').send_keys('033147')
    driver.find_element(by=By.ID, value='ctl00_cphMain_txtUsername').send_keys('supatel')
    driver.find_element(by=By.ID, value='ctl00_cphMain_txtPassword').send_keys('CMTInc2017!')
    driver.find_element(by=By.ID, value='btnLogin').click()
    time.sleep(5)
    driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Settings').click()
    driver.find_element(by=By.PARTIAL_LINK_TEXT, value='buyers guides').click()
    driver.find_element(by=By.PARTIAL_LINK_TEXT, value='Vehicle History Reports').click()
    driver.find_element(by=By.XPATH, value='//button[contains(text(),"Upgraded Reports")]').click()
    #driver.find_element(by=By.XPATH, value='//button[contains(text(),"Close")]').click()
    #driver.find_element(by=By.XPATH, value='//button[contains(text(),"Log Out")]').click()


finally:
    # driver.find_element(by=By.NAME, value='Log out of WebManager').click()
    driver.quit()


    cookies_list = driver.get_cookies()
    cookies_dict = {}

    for cookie in cookies_list:
        print("printing cookie\n")
        print(cookie)
        print(cookie['name'])
        print(cookie['value'])
        cookies_dict[cookie['name']] = cookie['value']

    session_id = cookies_dict.get('session')
    print(session_id)

    for keys, values in cookies_dict.items():
        print(keys)
        print(values)

'''


class MyClass(object):

    def __init__(self):
        t = "my"
        print(t)


class ChildClass(MyClass):

    def __init__(self):
        super(ChildClass, self).__init__()
        self.t = "mymy"
        print(self.t)


obj = ChildClass()

