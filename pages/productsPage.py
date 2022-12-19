from selenium import webdriver
from selenium.webdriver.common.by import By
from loginPage import *
import time

class productsPage():
    
    def addItemsToCart():
        items = ("backpack", "bike-light", "bolt-t-shirt", "fleece-jacket")
        for item in items:
            product = driver.find_element(By.ID, "add-to-cart-sauce-labs-" + item)
            product.click()

    def clickOnCartIcon():
        cartIcon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cartIcon.click()