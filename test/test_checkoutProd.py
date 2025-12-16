import pytest
from page.login_page import LoginPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage

@pytest.mark.usefixtures("driver")
def test_checkout(driver):
    # Paso 1: Login inicial
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Paso 2: Agregar producto al carrito
    cart_page = CartPage(driver)
    cart_page.agregar_producto("Sauce Labs Backpack")
    assert cart_page.verificar_producto_en_carrito("Sauce Labs Backpack")

    # Paso 3: Ir al carrito
    cart_page.ir_al_carrito()

    # Paso 4: Click en el botón Checkout
    cart_page.click_checkout()

    # Paso 5: Completar datos de envío
    checkout_page = CheckoutPage(driver)
    checkout_page.completar_datos_envio("Maria", "Marchi", "1234")

    # Paso 6: Confirmar compra
    checkout_page.confirmar_compra()

    # Paso 7: Validar confirmación
    assert checkout_page.verificar_confirmacion()
