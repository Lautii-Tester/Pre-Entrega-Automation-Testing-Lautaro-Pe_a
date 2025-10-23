import pytest #Importamos pytest para gestionar los tests
from selenium import webdriver  #Importamos la librería que permite controlar el navegador
from selenium.webdriver.common.by import By #Importamos la clase By para localizar elementos
from selenium.webdriver.common.keys import Keys #Importamos la clase Keys para simular teclas especiales
from selenium.webdriver.edge.options import Options #Importamos las opciones para Edge
from selenium.webdriver.edge.service import Service #Importamos el servicio para Edge
from selenium.webdriver.support import expected_conditions as EC #Importamos las condiciones esperadas para las esperas explícitas
from selenium.webdriver.support.ui import WebDriverWait #Importamos WebDriverWait para esperas explícitas
import time  #Para hacer pausas visibles


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized") #Abre ventana maximizada de Edge
    edge_service = Service()  #Usa el servicio por defecto de Edge
    driver = webdriver.Edge(options=options,service=edge_service) #Creamos la instancia del driver que abre una ventana de Edge con opciones
    driver.implicitly_wait(5) #Espera implícita de 5 segundos
    yield driver
    driver.quit()  #Cierra la ventana al finalizar el test

def test_swag_labs(driver):
    #1. Login
    driver.get("https://www.saucedemo.com")  #Accedemos a la URL de Sauce Demo
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    #2. Validar que estamos en inventario
    assert "/inventory.html" in driver.current_url
    
    #3. Verificar título de sección
    titulo = driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text
    assert titulo == "Products"
    
    #4. Contar productos visibles
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0

    #5. Añadir el primer producto al carrito
    productos[0].find_element(By.TAG_NAME, "button").click()
 
    #6. Confirmar que el badge del carrito muestra 1
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "1"

    #7. Detectar varios elementos de la interfaz
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_link").is_displayed()
    assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed()

    time.sleep(5)  #Pausa de 5s para ver los elementos antes de entrar al carrito

    #8 Entrar al carrito y verificar el producto añadido
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_item = WebDriverWait (driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_item")))
    assert cart_item.is_displayed()

    time.sleep(5)  #Pausa de 5s para que lo veas antes de cerrar