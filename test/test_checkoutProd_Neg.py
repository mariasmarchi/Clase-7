import pytest
from page.checkout_page import CheckoutPage

@pytest.mark.usefixtures("driver")
def test_checkout_sin_productos(driver):
    checkout = CheckoutPage(driver)

    # Intentar completar datos de envío sin productos en el carrito
    checkout.completar_datos_envio("Maria", "Marchi", "1234")
    checkout.confirmar_compra()

    # Verificar que no se pueda finalizar la compra
    assert not checkout.verificar_confirmacion()
