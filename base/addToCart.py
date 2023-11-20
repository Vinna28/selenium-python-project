
from pageObject.page.productPage import productPage
from pageObject.page.cartPage import cartPage

def test_add_product_to_cart(driver):
    driver.find_element(*productPage.addToCartButton).click()
    driver.find_element(*cartPage.cartIcon).click()