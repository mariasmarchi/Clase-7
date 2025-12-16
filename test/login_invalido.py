import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("driver")
def test_login_invalido(driver):
    login = LoginPage(driver)
    login.ir_a_login()
    login.login("usuario_falso", "clave_incorrecta")

    assert login.mensaje_error_visible(), "No apareció mensaje de error en login inválido"
