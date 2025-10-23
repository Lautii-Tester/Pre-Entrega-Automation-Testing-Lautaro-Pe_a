import pytest
from selenium import webdriver  
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.edge.options import Options 
from selenium.webdriver.edge.service import Service 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait 
import time 
import os

@pytest.fixture
def driver(driver):
    options = Options()
    service = Service()
    driver = webdriver.Edge(service=service, options=options)
    options.add_argument ("--start-maximized") #Abre ventana maximizada de Edge
    driver.implicitly_wait(5) #Espera implícita de 5 segundos
    yield driver
    driver.quit()
