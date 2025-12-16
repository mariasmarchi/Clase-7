from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.items = (By.CLASS_NAME, "inventory_item")
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.item_price = (By.CLASS_NAME, "inventory_item_price")
        self.add_to_cart_button = (By.CLASS_NAME, "btn_inventory")
        self.cart_icon = (By.ID, "shopping_cart_container")

    def obtener_productos(self):
        return self.driver.find_elements(*self.items)

    def agregar_producto_por_indice(self, index=0):
        botones = self.driver.find_elements(*self.add_to_cart_button)
        botones[index].click()

    def ir_al_carrito(self):
        self.driver.find_element(*self.cart_icon).click()
