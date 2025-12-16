from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def agregar_producto(self, nombre_producto):
        # Encuentra el botón "Add to cart" del producto y lo hace click
        boton = self.driver.find_element(
            By.XPATH,
            f"//div[text()='{nombre_producto}']/ancestor::div[@class='inventory_item']//button"
        )
        boton.click()

    def verificar_producto_en_carrito(self, nombre_producto):
        # Verifica que el producto esté listado en el carrito
        return nombre_producto in self.driver.page_source
