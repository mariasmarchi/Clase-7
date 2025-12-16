from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")

    def completar_datos_envio(self, nombre, apellido, codigo_postal):
        self.driver.find_element(*self.first_name).send_keys(nombre)
        self.driver.find_element(*self.last_name).send_keys(apellido)
        self.driver.find_element(*self.postal_code).send_keys(codigo_postal)
        self.driver.find_element(*self.continue_button).click()

    def confirmar_compra(self):
        self.driver.find_element(*self.finish_button).click()

    def verificar_confirmacion(self):
        return "Thank you for your order!" in self.driver.page_source
