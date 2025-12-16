import pytest
from page.inventory_page import InventoryPage

def test_busqueda_producto(driver):
    inventory_page = InventoryPage(driver)

    # Verificar que un producto esperado esté visible en el inventario
    assert inventory_page.verificar_producto_visible("Sauce Labs Backpack")
