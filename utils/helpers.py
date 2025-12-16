import os
import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://www.saucedemo.com'
USERNAME = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():
    # Configuración del driver con webdriver_manager
    service = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument("--start-maximized")  # abrir maximizado
    driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(10)  # espera implícita
    return driver

def login_saucedemo(driver):
    driver.get(URL)

    # Ingresar credenciales
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'user-name'))
    ).send_keys(USERNAME)

    driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
    driver.find_element(By.ID, 'login-button').click()

def get_file_path(file_name, folder="data"):
    # Ruta relativa al archivo dentro de la carpeta data
    current_file = os.path.dirname(__file__)
    file_path = os.path.join(current_file, "..", folder, file_name)
    return os.path.abspath(file_path)

def leer_datos_csv(ruta_csv):
    """
    Lee un archivo CSV y devuelve una lista de tuplas (usuario, clave).
    El CSV debe tener dos columnas: usuario, clave.
    """
    datos = []
    with open(ruta_csv, newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        next(lector, None)  # saltar encabezado si existe
        for fila in lector:
            if len(fila) >= 2:
                usuario, clave = fila[0], fila[1]
                datos.append((usuario, clave))
    return datos
