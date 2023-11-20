from selenium.webdriver.common.by import By

class cartPage():
    cartIcon = (By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cartHeader = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
    cartTitle = "Your Cart"
    cartItem = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]/div[1]')
    cartContent = "1"
    cartRemoveBtn = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')
    continueShoppingBtn = (By.XPATH, '//*[@id="continue-shopping"]')
    checkoutBtn = (By.XPATH, '//*[@id="checkout"]')
    checkoutHeader =(By.XPATH, '//*[@id="header_container"]/div[2]/span')
    cartContainer = (By.XPATH, '//*[@id="cart_contents_container"]/div/div[1]/div[3]')
    checkoutTitle = "Checkout: Your Information"