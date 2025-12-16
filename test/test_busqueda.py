import pytest
from page.inventory_page import InventoryPage

def test_busqueda_producto(driver):
    # Abrir la página de inventario
    inventory_page = InventoryPage(driver)
    inventory_page.open()

    # Verificar que un producto esperado esté visible
    assert inventory_page.verificar_producto_visible("Sauce Labs Backpack")
