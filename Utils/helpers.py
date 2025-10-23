from selenium import webdriver 
from selenium.webdriver.support import expected_conditions as EC #Importamos las condiciones esperadas para las esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait #Importamos WebDriverWait para esperas explícitas
from selenium.webdriver.common.by import By

class login:
    URL = "https://www.saucedemo.com"
    USERNAME = "standard_user"
    PASSWORD = "secret_sauce"
    LOGIN_BUTTON = (By.ID, "login-button").click()

def tiempo_espera (driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

class InventoryPageLocators:
    TITLE = (By.CSS_SELECTOR, "div.header_secondary_container .title")
    PRODUCTS = (By.CLASS_NAME, "inventory_item")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    