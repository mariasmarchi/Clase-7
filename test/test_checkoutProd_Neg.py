import pytest
from page.checkout_page import CheckoutPage

#Checkout sin productos (negativo extra)
@pytest.mark.usefixtures("driver")
def test_checkout_sin_productos(driver):
    checkout = CheckoutPage(driver)
    checkout.ir_a_checkout()

    assert checkout.mensaje_carrito_vacio(), "Se permitió checkout sin productos en el carrito"
