import pytest
from pages.search_page import SearchPage
from pages.cart_page import CartPage

#añadir producto al carrito
@pytest.mark.usefixtures("driver")
def test_agregar_producto_al_carrito(driver):
    search = SearchPage(driver)
    search.ir_a_busqueda("t-shirt")
    search.seleccionar_producto(0)  # primer producto
    search.agregar_al_carrito()

    cart = CartPage(driver)
    assert cart.verificar_producto_en_carrito("t-shirt"), "El producto no se agregó al carrito"
