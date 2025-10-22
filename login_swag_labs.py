from selenium import webdriver  #Importamos la librería que permite controlar el navegador
import time  #Para hacer pausas visibles
from selenium.webdriver.common.by import By #Importamos la clase By para localizar elementos
from selenium.webdriver.common.keys import Keys #Importamos la clase Keys para simular teclas especiales
from selenium.webdriver.edge.options import Options #Importamos las opciones para Edge
from selenium.webdriver.support.ui import WebDriverWait #Importamos WebDriverWait para esperas explícitas
from selenium.webdriver.support import expected_conditions as EC #Importamos las condiciones esperadas para las esperas explícitas

options = Options()
options.add_argument("--start-maximized") #Abre ventana maximizada de Edge
driver = webdriver.Edge(options=options) #Creamos la instancia del driver que abre una ventana de Edge con opciones
driver.implicitly_wait(5) #Espera implícita de 5 segundos

try:
    #1. Login
    driver.get("https://www.saucedemo.com")  #Accedemos a la URL de Sauce Demo (pantalla de login)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
    
    #2. Validar que estamos en inventario
    assert "/inventory.html" in driver.current_url
    print("Login OK →", driver.current_url)
    
    #3. Verificar título de sección
    titulo = driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text
    assert titulo == "Products"
    print("Título de sección OK →", titulo)
    
    #4. Contar productos visibles
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    print(f"Se encontraron {len(productos)} productos.")
 
    #5. Añadir el primer producto al carrito
    productos[0].find_element(By.TAG_NAME, "button").click()
 
    #6. Confirmar que el badge del carrito muestra 1
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "1"
    print("Carrito OK →", badge)

    #7. Detectar varios elementos de la interfaz
    boton_menu = driver.find_element(By.ID, "react-burger-menu-btn")
    print("Botón menú encontrado →", boton_menu.is_displayed())
    boton_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    print("Botón carrito encontrado →", boton_carrito.is_displayed())
    boton_product_container = driver.find_element(By.CLASS_NAME, "product_sort_container")
    print("Contenedor de productos encontrado →", boton_product_container.is_displayed())

    #8 Entrar al carrito y verificar el producto añadido
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    cart_item = WebDriverWait (driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_item")))
    print("Producto en carrito OK →", cart_item.is_displayed())

    time.sleep(5)  #Pausa de 5s para que lo veas antes de cerrar

finally:
    driver.quit()  #Cierre limpio: cierra la sesión y la ventana 