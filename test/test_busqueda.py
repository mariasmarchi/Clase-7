import pytest
from page.login_page import LoginPage
from page.inventory_page import InventoryPage

def test_busqueda_producto(driver):
    # Paso 1: Login inicial
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    # Paso 2: Validar que el producto esté visible en inventario
    inventory_page = InventoryPage(driver)
    assert inventory_page.verificar_producto_visible("Sauce Labs Backpack")
