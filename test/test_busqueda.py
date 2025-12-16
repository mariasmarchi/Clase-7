import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage

#busqueda de producto
@pytest.mark.usefixtures("driver")
def test_busqueda_producto(driver):
    home = HomePage(driver)
    home.ir_a_home()
    home.buscar_producto("dress")

    search = SearchPage(driver)
    resultados = search.obtener_resultados()
    assert len(resultados) > 0, "No se encontraron productos en la búsqueda"
