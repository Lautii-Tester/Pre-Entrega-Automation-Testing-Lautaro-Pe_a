import pytest
import time 
import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utils.helpers import login as loc
from Utils.helpers import InventoryPageLocators as inv
from Utils.helpers import tiempo_espera
from Tests.confest import driver

@pytest.fixture(scope="session")
def login_sauce(driver): #1. Testeo de login
    driver.get(*loc.URL)  #Accedemos a la URL de Sauce Demo (pantalla de login)
    driver.find_element(*loc.USERNAME).send_keys("standard_user")
    driver.find_element(*loc.PASSWORD).send_keys("secret_sauce")
    driver.find_element(*loc.LOGIN_BUTTON).click()

    #2. Validar que estamos en inventario
    assert "/inventory.html" in driver.current_url
   
    #3. Verificar título de sección
    titulo = tiempo_espera(driver, inv.TITLE)
    assert titulo.text == "Products"

    time.sleep(3)  #Pausa de 3s para ver el login antes de continuar
    return driver
if __name__ == "__main__":
    login_sauce()