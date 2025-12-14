from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  #llamar  los selectores
from selenium.webdriver.common.keys import Keys  #pasar datos
from selenium.webdriver.chrome.service import Service
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://duckduckgo.com/")
time.sleep(5)  # Espera para asegurar que la página se cargue completamente

buscar = "Selenium Python"
cuadro_buscar = driver.find_element(By.NAME, "q")
cuadro_buscar.send_keys(buscar)
cuadro_buscar.send_keys(Keys.RETURN)  # Simula presionar la tecla Enter
driver.save_screenshot('busquedaSelenium.png')
time.sleep(7)  # Espera para ver los resultados de la búsqueda


primer_result = driver.find_element(By.CLASS_NAME, 'eVNpHGjtxRBq_gLOfGDr ')
url_result = primer_result.get_attribute('href')
primer_result.click()

time.sleep(7)  # Espera para ver la página del primer resultado