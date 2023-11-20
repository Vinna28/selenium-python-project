import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pageObject.page.loginPage import loginPage
from pageObject.page.productPage import productPage
from pageObject.data.loginData import inputLoginData
from pageObject.page.cartPage import cartPage
from base import baseLogin
from base import addToCart


class CartTesting(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        self.url = "https://www.saucedemo.com/"

    # def test_show_cart_page(self):
    #     driver = self.browser
    #     driver.get(self.url)
    #     baseLogin.test_login(driver, inputLoginData.standardUser, inputLoginData.validPassword)
    #     driver.find_element(*cartPage.cartIcon).click()

    #     response = driver.find_element(*cartPage.cartHeader).text
    #     self.assertIn(cartPage.cartTitle, response)

    #     driver.close()

    # def test_show_cart_item(self):
    #     driver = self.browser
    #     driver.get(self.url)
    #     baseLogin.test_login(driver, inputLoginData.standardUser, inputLoginData.validPassword)
    #     addToCart.test_add_product_to_cart(driver)

    #     response = driver.find_element(*cartPage.cartItem).text
    #     self.assertIn(cartPage.cartContent, response)

    #     driver.close()

    # def test_continue_shopping(self):
    #     driver = self.browser
    #     driver.get(self.url)
    #     baseLogin.test_login(driver, inputLoginData.standardUser, inputLoginData.validPassword)
    #     addToCart.test_add_product_to_cart(driver)
    #     driver.find_element(*cartPage.continueShoppingBtn).click()

    #     response = driver.find_element(*loginPage.afterLogin).text
    #     self.assertIn(loginPage.validLoginTitle, response)

    #     driver.close()

    def test_remove_cart_item(self):
        driver = self.browser
        driver.get(self.url)
        baseLogin.test_login(driver, inputLoginData.standardUser, inputLoginData.validPassword)
        addToCart.test_add_product_to_cart(driver)
        driver.find_element(*cartPage.cartRemoveBtn).click()

        response = driver.find_element(*cartPage.cartContainer).clear
        self.assertTrue(response)

        driver.close()

    def test_show_checkout(self):
        driver = self.browser
        driver.get(self.url)
        baseLogin.test_login(driver, inputLoginData.standardUser, inputLoginData.validPassword)
        addToCart.test_add_product_to_cart(driver)
        driver.find_element(*cartPage.checkoutBtn).click()

        response = driver.find_element(*cartPage.checkoutHeader).text
        self.assertIn(cartPage.checkoutTitle, response)

        driver.close()

if __name__ == "__main__":
    unittest.main()