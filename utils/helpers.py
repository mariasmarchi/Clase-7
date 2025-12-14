from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By  #llamar  los selectores
from selenium.webdriver.chrome.options import Options #para el navegador
#from selenium.webdriver.common.keys import Keys  #pasar datos
from selenium.webdriver.chrome.service import Service
#import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL= 'https://www.saucedemo.com'
USERNAME= 'standard_user'
PASSWORD= 'secret_sauce'

def get_driver():
    #chrome_options = Options()
    #chrome_options.add_experimental_option("detach", True) #para que no se cierre el navegador
    #options = Options()
    #options.add_argument(--start-maximized)  #para que se abra maximizado

    #instalar el driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service,) #options=chrome_options)

    #time.sleep(5)
    driver.implicitly_wait(10) #resuelve el test y si dura mas de 5 segundos dara error, tambien si dura menos de 5 seg corta cuando termina de ejecutar, no espera a completar el tiempo.

    return driver

def login_saucedemo( driver ):
    driver.get(URL)
    
    #Ingresar las credenciales
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, 'user-name'))
    ).send_keys(USERNAME)


    #driver.find_element(By.NAME, 'user-name').send_keys(USERNAME)
    driver.find_element(By.NAME, 'password').send_keys(PASSWORD)
    driver.find_element(By.ID, 'login-button').click()
    #time.sleep(7)