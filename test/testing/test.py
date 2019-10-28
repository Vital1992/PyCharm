import unittest
from testing.elements import *
from testing import loginFunction
from testing import registartionFunction

class Login(unittest.TestCase):

    def setUp(self):
        driver = self.driver = pom.driver
        driver.maximize_window()
        driver.get("https://www.toyotanation.com/forums/")

    def test_login(self):
        driver = self.driver
        login = loginFunction.loginModule(driver)
        login.test_login(users.login1, users.password1) #username and password can be changed to test multiple accounts

    def tearDown(self):
        self.driver.quit()

class CreateAccount(unittest.TestCase):

    def setUp(self):
        driver = self.driver = pom.driver
        driver.maximize_window()
        driver.get("https://www.toyotanation.com/forums/")

    def test_registration(self):
        driver = self.driver
        registration = registartionFunction.registerModule(driver)
        registration.test_create_account("QATester1", "qagrabtester3@gmail.com", "Qa123456789!")

    def tearDown(self):
        self.driver.quit()