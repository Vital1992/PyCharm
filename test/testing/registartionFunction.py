import unittest
from time import sleep
from selenium.webdriver.common.by import By
from testing.elements import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class registerModule():

    def __init__(self, driver):
        self.driver = driver

    def setUp(self):
        driver = self.driver = pom.driver
        driver.maximize_window()
        driver.get("https://www.toyotanation.com/forums/")

    def test_create_account(self, usernameInput, emailInput, passwordInput):
        driver = self.driver
        login_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, pom.loginBtn)))
        login_btn.click()

        register_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, pom.registerBtn)))
        register_btn.click()

        username = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, pom.usernameFiled)))
        username.send_keys(usernameInput)

        email = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, pom.emailField)))
        email.send_keys(emailInput)

        driver.find_element_by_xpath(pom.passwordFiled).send_keys(passwordInput)

        driver.find_element_by_xpath(pom.acceptTerms).click()

        sleep(11)

        driver.find_element_by_xpath(pom.submitBtn).click()

        sleep(3)

        driver.find_element_by_xpath(pom.successfulRegistration)
