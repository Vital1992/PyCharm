from time import sleep
from testing.elements import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class loginModule():

    def __init__(self, driver):
        self.driver = driver

    def test_login(self, username, password):
        driver = self.driver
        login_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, pom.loginBtn)))
        login_btn.click()

        login_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, pom.loginUsernameField)))
        login_field.send_keys(username)

        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, pom.loginPasswordField)))
        password_field.send_keys(password)

        driver.find_element_by_xpath(pom.loginBtn2).click()

        account_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, pom.userIcon)))
        account_btn.click()

        profile_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, pom.userProfile)))
        profile_btn.click()

        driver.find_element_by_xpath("//span[text()='QATest1']")
