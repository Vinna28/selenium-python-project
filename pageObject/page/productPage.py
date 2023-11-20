from selenium.webdriver.common.by import By

class productPage():
    productTitle = (By.XPATH, '//*[@id="item_4_title_link"]/div')
    productPrice = (By.CSS_SELECTOR, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
    detailProduct = (By.XPATH, '//*[@id="back-to-products"]')
    detailProductHeader = "Back to products"
    addToCartButton = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    shoppingCartBadge = (By.XPATH, '//*[@id="shopping_cart_container"]/a/span')
    removeButton = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    addToCartName = "Add to cart"
    productFilter = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
    lowToHighPriceFilter = (By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[3]')