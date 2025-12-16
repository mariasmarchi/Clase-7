import pytest
from page.cart_page import CartPage

@pytest.mark.usefixtures("driver")
def test_agregar_producto_al_carrito(driver):
    cart_page = CartPage(driver)

    # Agregar un producto al carrito
    cart_page.agregar_producto("Sauce Labs Backpack")

    # Verificar que el producto esté en el carrito
    assert cart_page.verificar_producto_en_carrito("Sauce Labs Backpack")
