# POM for login steps

from pageObject.page.loginPage import loginPage

def test_login(driver, loginUsername, loginPassword):
    driver.find_element(*loginPage.username).send_keys(loginUsername)
    driver.find_element(*loginPage.password).send_keys(loginPassword)
    driver.find_element(*loginPage.loginButton).click()