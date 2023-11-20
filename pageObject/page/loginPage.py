# POM for base login page

from selenium.webdriver.common.by import By

class loginPage ():
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    loginButton = (By.ID, "login-button")
    afterLogin = (By.XPATH, "(//span[@class='title'])[1]")
    errorLogin = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
    validLoginTitle = "Products"
    lockedLoginMsg = "Epic sadface: Sorry, this user has been locked out."
    failedLoginMsg = "Epic sadface: Username and password do not match any user in this service"
    usernameEmptyMsg = "Epic sadface: Username is required"
    passwordEmptyMsg = "Epic sadface: Password is required"