import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pageObject.page.loginPage import loginPage
from pageObject.page.productPage import productPage
from pageObject.data.loginData import inputLoginData
from base import baseLogin
import HtmlTestRunner

class ProductTesting(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.url = "https://www.saucedemo.com/"

    def test_show_all_product(self):
        driver = self.browser
        driver.get(self.url)
        baseLogin.test_login(driver, inputLoginData.standardUser, inputLoginData.validPassword)

        response = driver.find_element(*loginPage.afterLogin).text
        self.assertIn(loginPage.validLoginTitle, response)

        driver.close()

    def test_show_detail_product(self):
        driver = self.browser
        driver.get(self.url)
        baseLogin.test_login(driver, inputLoginData.standardUser, inputLoginData.validPassword)
        driver.find_element(*productPage.productTitle).click()

        response = driver.find_element(*productPage.detailProduct).text
        self.assertIn(productPage.detailProductHeader, response)

        driver.close()

    def test_add_to_cart(self):
        driver = self.browser
        driver.get(self.url)
        baseLogin.test_login(driver, inputLoginData.standardUser, inputLoginData.validPassword)
        driver.find_element(*productPage.addToCartButton).click()

        response = driver.find_element(*productPage.shoppingCartBadge).is_enabled
        self.assertTrue(response)
        driver.close()

    def test_remove_shopping_cart(self):
        driver = self.browser
        driver.get(self.url)
        baseLogin.test_login(driver, inputLoginData.standardUser, inputLoginData.validPassword)
        driver.find_element(*productPage.addToCartButton).click()
        driver.find_element(*productPage.removeButton).click()

        response = driver.find_element(*productPage.addToCartButton).text
        self.assertIn(productPage.addToCartName, response)
        driver.close()


if __name__ == "__main__":
    unittest.main()
    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='result'))