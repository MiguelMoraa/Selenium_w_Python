from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path = r"C:\dChrome\chromedriver_win32.exe")
driver.get("https://www.saucedemo.com/")
usernameField = driver.find_element(By.ID, "user-name")
passwordField = driver.find_element(By.ID, "password")
enterButton = driver.find_element(By.ID, "login-button")

class loginPage():

    def fillLoginForm(user, password,):
        usernameField.send_keys(user)
        passwordField.send_keys(password)
        enterButton.click()
        time.sleep(3)
        driver.close()