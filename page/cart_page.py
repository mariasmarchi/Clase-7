from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.items = (By.CLASS_NAME, "cart_item")
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.checkout_button = (By.ID, "checkout")

    def obtener_items(self):
        return self.driver.find_elements(*self.items)

    def verificar_producto_en_carrito(self, nombre_producto):
        nombres = [el.text for el in self.driver.find_elements(*self.item_name)]
        return nombre_producto in nombres

    def ir_a_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
