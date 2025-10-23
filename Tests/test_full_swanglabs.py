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

def login_sauce(driver): #1. Testeo de login, redirigir al inventario, verificar título
    driver.get(*loc.URL)  #Accedemos a la URL de Sauce Demo (pantalla de login)
    driver.find_element(*loc.USERNAME).send_keys("standard_user")
    driver.find_element(*loc.PASSWORD).send_keys("secret_sauce")
    driver.find_element(*loc.LOGIN_BUTTON).click()

def test_catalogo(driver): #2. Validar que estamos en inventario
    from selenium.webdriver.common.by import By
    assert "/inventory.html" in driver.current_url

    #3. Verificar título de sección
    titulo = tiempo_espera(driver, inv.TITLE)
    assert titulo.text == "Products"

    #4. Contar productos visibles
    productos = driver.find_elements(*inv.PRODUCTS)
    assert len(productos) > 0       

def test_elementos_interfaz(driver): #5. Detectar varios elementos de la interfaz
    from selenium.webdriver.common.by import By
    boton_menu = driver.find_element(By.ID, "react-burger-menu-btn")
    assert boton_menu.is_displayed()
    boton_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    assert boton_carrito.is_displayed()
    boton_product_container = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert boton_product_container.is_displayed()

def test_carrito(driver): #6. Añadir el primer producto al carrito
    from selenium.webdriver.common.by import By
    productos = driver.find_elements(*inv.PRODUCTS)
    assert len(productos) > 0
    productos[0].find_element("tag name", "button").click()
    
    #7. Confirmar que el badge del carrito muestra 1
    badge = driver.find_element(*inv.CART_BADGE)
    assert badge.text == "1"

    #8. Entrar al carrito y verificar el producto añadido
    driver.find_element(*inv.CART_LINK).click()
    cart_item = tiempo_espera (driver,cart_item)
    assert cart_item.is_displayed()
    
    time.sleep(3)  #Pausa de 3s para ver el login antes de continuar
    return driver
if __name__ == "__main__":
    login_sauce()