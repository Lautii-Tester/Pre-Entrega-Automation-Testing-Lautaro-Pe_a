import pytest
import time
import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utils.helpers import login as loc
from Utils.helpers import tiempo_espera
from Utils.helpers import InventoryPageLocators as inv

def test_login(driver): #1. Login
    driver.get(loc.URL)  #Accedemos a la URL de Sauce Demo (pantalla de login)
    driver.find_element(*loc.USERNAME_INPUT).send_keys(loc.USERNAME)
    driver.find_element(*loc.PASSWORD_INPUT).send_keys(loc.PASSWORD)
    driver.find_element(*loc.LOGIN_BUTTON).click()

def test_carrito(driver): #2. Añadir el primer producto al carrito
    productos = driver.find_elements(*inv.PRODUCTS)
    assert len(productos) > 0
    productos[0].find_element("tag name", "button").click()
 
    #3. Confirmar que el badge del carrito muestra 1
    badge = driver.find_element(*inv.CART_BADGE)
    assert badge.text == "1"

    #4. Entrar al carrito y verificar el producto añadido
    driver.find_element(*inv.CART_LINK).click()
    cart_item = tiempo_espera (driver, inv.CART_ITEM)
    assert cart_item.is_displayed()

    time.sleep(5)  #Pausa de 5s para que lo veas antes de cerrar