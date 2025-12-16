import pytest
from page.checkout_page import CheckoutPage

@pytest.mark.usefixtures("driver")
def test_checkout_sin_productos(driver):
    # Nota: este test valida que no se pueda finalizar la compra sin productos en el carrito
    checkout = CheckoutPage(driver)

    # Intentamos completar datos de envío sin productos
    checkout.completar_datos_envio("Maria", "Marchi", "1234")
    checkout.confirmar_compra()

    # Verificamos que la compra NO se haya completado
    assert not checkout.verificar_confirmacion()
