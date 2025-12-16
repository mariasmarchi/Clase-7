import pytest
from page.login_page import LoginPage
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage

@pytest.mark.usefixtures("driver")
def test_checkout_sin_productos(driver):
    # Paso 1: Login inicial
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Paso 2: Ir al carrito vacío
    cart_page = CartPage(driver)
    cart_page.ir_al_carrito()

    # Paso 3: Click en el botón Checkout
    cart_page.click_checkout()

    # Paso 4: Intentar completar datos de envío sin productos
    checkout_page = CheckoutPage(driver)
    checkout_page.completar_datos_envio("Maria", "Marchi", "1234")
    checkout_page.confirmar_compra()

    # Paso 5: Validar que la compra NO se haya completado
    assert not checkout_page.verificar_confirmacion()
