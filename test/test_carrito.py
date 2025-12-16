import pytest
from page.cart_page import CartPage

@pytest.mark.usefixtures("driver")
def test_agregar_producto_al_carrito(driver):
    # Nota: este test agrega un producto al carrito y valida que esté presente
    cart_page = CartPage(driver)

    # Agregamos el producto "Sauce Labs Backpack" al carrito
    cart_page.agregar_producto("Sauce Labs Backpack")

    # Verificamos que el producto se encuentra en el carrito
    assert cart_page.verificar_producto_en_carrito("Sauce Labs Backpack")
