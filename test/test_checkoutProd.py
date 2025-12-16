import pytest
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage

#Checkout / compra simulada
@pytest.mark.usefixtures("driver")
def test_checkout(driver):
    cart = CartPage(driver)
    cart.open_cart()
    cart.ir_a_checkout()

    checkout = CheckoutPage(driver)
    checkout.completar_datos_envio("Maria", "Marchi", "Buenos Aires")
    checkout.confirmar_compra()

    assert checkout.verificar_confirmacion(), "La compra no se completó correctamente"
