from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.helpers import URL, USERNAME, PASSWORD

class LoginPage:
    #USERNAME = 'standard_user'
    #PASSWORD = 'secret_sauce'
    # Selectores exactos de Saucedemo
    _INPUT_NAME = (By.ID, 'user-name')       # campo usuario
    _INPUT_PASSWORD = (By.ID, 'password')    # campo contraseña
    _LOGIN_BUTTON = (By.ID, 'login-button')  # botón login
    _ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")  # mensaje de error

    def __init__(self, driver):
        self.driver = driver
    
    def open(self):
        # Abre la página principal de login
        self.driver.get(URL)

    def login(self, username=USERNAME, password=PASSWORD):
        # Espera hasta que el campo usuario esté disponible y envía el texto
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._INPUT_NAME)   # valida si existe
        ).send_keys(username)                              # lo envía
        
        # Espera hasta que el campo contraseña esté disponible y envía el texto
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._INPUT_PASSWORD)  # valida si existe
        ).send_keys(password)                                 # lo envía

        # Espera hasta que el botón login esté disponible y hace click
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self._LOGIN_BUTTON)    # valida si existe
        ).click()                                            # hace click

        # Alternativa sin WebDriverWait:
        # self.driver.find_element(By.ID, 'user-name').send_keys(username)
        # self.driver.find_element(By.ID, 'password').send_keys(password)
        # self.driver.find_element(By.ID, 'login-button').click()

    def mensaje_error_visible(self):
        # Devuelve True si aparece el mensaje de error en login inválido
        return len(self.driver.find_elements(*self._ERROR_MESSAGE)) > 0
