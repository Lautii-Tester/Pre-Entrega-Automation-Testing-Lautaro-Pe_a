import pytest
import time
import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utils.helpers import login as loc
from Utils.helpers import tiempo_espera
from Utils.helpers import InventoryPageLocators as inv
from Tests.confest import driver

@pytest.fixture(scope="session")
def login_sauce(driver): #1. Login
    driver.get(*loc.URL)  #Accedemos a la URL de Sauce Demo (pantalla de login)
    driver.find_element(*loc.USERNAME).send_keys("standard_user")
    driver.find_element(*loc.PASSWORD).send_keys("secret_sauce")
    driver.find_element(*loc.LOGIN_BUTTON).click()

def test_carrito(driver): #2. Añadir el primer producto al carrito
    login_sauce(driver)
    productos = driver.find_elements(*inv.PRODUCTS)
    assert len(productos) > 0
    productos[0].find_element("tag name", "button").click()
 
    #3. Confirmar que el badge del carrito muestra 1
    badge = driver.find_element(*inv.CART_BADGE)
    assert badge.text == "1"

    #4. Entrar al carrito y verificar el producto añadido
    driver.find_element(*inv.CART_LINK).click()
    cart_item = tiempo_espera (driver,cart_item)
    assert cart_item.is_displayed()

    time.sleep(5)  #Pausa de 5s para que lo veas antes de cerrar

    driver.quit()  #Cierre limpio: cierra la sesión y la ventana
if __name__ == "__main__":
    login_sauce()
