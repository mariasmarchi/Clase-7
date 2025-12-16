from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def verificar_producto_visible(self, nombre_producto):
        try:
            self.driver.find_element(By.XPATH, f"//div[text()='{nombre_producto}']")
            return True
        except:
            return False
