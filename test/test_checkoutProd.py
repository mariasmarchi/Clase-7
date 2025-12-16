import pytest
from page.cart_page import CartPage
from page.checkout_page import CheckoutPage

@pytest.mark.usefixtures("driver")
def test_checkout(driver):
    # Nota: este test simula un flujo de compra completo
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # Paso 1: Agregar producto al carrito
    cart_page.agregar_producto("Sauce Labs Backpack")
    assert cart_page.verificar_producto_en_carrito("Sauce Labs Backpack")

    # Paso 2: Completar datos de envío
    checkout_page.completar_datos_envio("Maria", "Marchi", "1234")

    # Paso 3: Confirmar la compra
    checkout_page.confirmar_compra()

    # Paso 4: Validar que la compra se haya completado
    assert checkout_page.verificar_confirmacion()
