from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, usuario, clave):
        self.driver.find_element(*self.username_input).send_keys(usuario)
        self.driver.find_element(*self.password_input).send_keys(clave)
        self.driver.find_element(*self.login_button).click()

    def verificar_login_exitoso(self):
        # Si aparece la página de inventario
        return "inventory.html" in self.driver.current_url

    def verificar_login_fallido(self):
        try:
            self.driver.find_element(By.CLASS_NAME, "error-message-container")
            return True
        except:
            return False
