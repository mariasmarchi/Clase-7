import pytest
from page.login_page import LoginPage
from page.cart_page import CartPage

@pytest.mark.usefixtures("driver")
def test_agregar_producto_al_carrito(driver):
    # Paso 1: Login inicial
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Paso 2: Agregar producto al carrito
    cart_page = CartPage(driver)
    cart_page.agregar_producto("Sauce Labs Backpack")

    # Paso 3: Validar que el producto esté en el carrito
    assert cart_page.verificar_producto_en_carrito("Sauce Labs Backpack")
