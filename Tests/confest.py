import pytest
from selenium import webdriver  
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.edge.options import Options 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait 

@pytest.fixture
def driver():
    options = Options()
    options.add_argument ("--start-maximized") #Abre ventana maximizada de Edge
    driver = webdriver.Edge(options=options)
    driver.implicitly_wait(5) #Espera implícita de 5 segundos
    yield driver
    driver.quit()