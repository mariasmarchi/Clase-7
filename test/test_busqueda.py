import pytest
from page.inventory_page import InventoryPage

def test_busqueda_producto(driver):
    # Nota: este test valida que un producto específico esté visible en el inventario
    inventory_page = InventoryPage(driver)

    # Verificamos que el producto "Sauce Labs Backpack" aparece en la lista
    assert inventory_page.verificar_producto_visible("Sauce Labs Backpack")
