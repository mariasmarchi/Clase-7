from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.checkout_button = (By.ID, "checkout")

    def agregar_producto(self, nombre_producto):
        boton = self.driver.find_element(
            By.XPATH,
            f"//div[text()='{nombre_producto}']/ancestor::div[@class='inventory_item']//button"
        )
        boton.click()

    def verificar_producto_en_carrito(self, nombre_producto):
        return nombre_producto in self.driver.page_source

    def ir_al_carrito(self):
        self.driver.find_element(*self.cart_icon).click()

    def click_checkout(self):
        # Hace click en el botón "Checkout" dentro del carrito
        self.driver.find_element(*self.checkout_button).click()
