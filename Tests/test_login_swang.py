import pytest
import time 
import sys 
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Utils.helpers import login as loc
from Utils.helpers import InventoryPageLocators as inv
from Utils.helpers import tiempo_espera


def test_login(driver): #1. Testeo de login
    driver.get(loc.URL)  #Accedemos a la URL de Sauce Demo (pantalla de login)
    driver.find_element(*loc.USERNAME_INPUT).send_keys(loc.USERNAME)
    driver.find_element(*loc.PASSWORD_INPUT).send_keys(loc.PASSWORD)
    driver.find_element(*loc.LOGIN_BUTTON).click()

    #2. Validar que estamos en inventario
    assert "/inventory.html" in driver.current_url
   
    #3. Verificar título de sección
    titulo = tiempo_espera(driver, inv.TITLE)
    assert titulo.text == "Products"

    time.sleep(3)  #Pausa de 3s para ver el login antes de continuar