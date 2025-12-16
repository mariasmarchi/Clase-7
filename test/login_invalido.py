import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("driver")
def test_checkout(driver):
    cart = CartPage(driver)
    cart.ir_al_carrito()
    cart.ir_a_checkout()

    checkout = CheckoutPage(driver)
    checkout.completar_datos_envio("Maria", "Marchi", "Buenos Aires")
    checkout.confirmar_compra()

    assert checkout.verificar_confirmacion(), "La compra no se completó correctamente"
