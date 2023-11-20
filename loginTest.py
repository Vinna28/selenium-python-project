import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pageObject.page.loginPage import loginPage
from pageObject.data.loginData import inputLoginData
from base import baseLogin
import HtmlTestRunner

class LoginTesting(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.url = "https://www.saucedemo.com/"

    def test_a_success_login(self):
        driver = self.browser
        driver.get(self.url)
        baseLogin.test_login(driver, inputLoginData.standardUser, inputLoginData.validPassword)

        response = driver.find_element(*loginPage.afterLogin).text
        self.assertIn(loginPage.validLoginTitle, response)

        driver.close()

    def test_locked_out_login(self):
        driver = self.browser
        driver.get(self.url)
        baseLogin.test_login(driver, inputLoginData.lockedUser, inputLoginData.validPassword)

        response = driver.find_element(*loginPage.errorLogin).text
        self.assertIn(loginPage.lockedLoginMsg, response)

        driver.close()

    def test_wrong_username(self):
        driver = self.browser
        driver.get(self.url)
        baseLogin.test_login(driver, inputLoginData.invalidUser, inputLoginData.validPassword)

        response = driver.find_element(*loginPage.errorLogin).text
        self.assertIn(loginPage.failedLoginMsg, response)

        driver.close()

    def test_wrong_password(self):
        driver = self.browser
        driver.get(self.url)
        baseLogin.test_login(driver, inputLoginData.standardUser, inputLoginData.invalidPassword)

        response = driver.find_element(*loginPage.errorLogin).text
        self.assertIn(loginPage.failedLoginMsg, response)

        driver.close()

    def test_username_empty(self):
        driver = self.browser
        driver.get(self.url)
        baseLogin.test_login(driver, "", inputLoginData.validPassword)

        response = driver.find_element(*loginPage.errorLogin).text
        self.assertIn(loginPage.usernameEmptyMsg, response)

        driver.close()

    def test_password_empty(self):
        driver = self.browser
        driver.get(self.url)
        baseLogin.test_login(driver, inputLoginData.standardUser, "")

        response = driver.find_element(*loginPage.errorLogin).text
        self.assertIn(loginPage.passwordEmptyMsg, response)

        driver.close()
    
if __name__ == "__main__":
    unittest.main()
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='result'))