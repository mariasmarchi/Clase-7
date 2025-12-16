import pytest
from page.login_page import LoginPage
from utils.helpers import leer_datos_csv

# Nota: este test parametriza el login con datos del CSV
@pytest.mark.parametrize("usuario,clave", leer_datos_csv("data/data_login.csv"))
def test_login_parametrizado(driver, usuario, clave):
    login_page = LoginPage(driver)

    # Paso 1: Abrir la página de login
    login_page.open()

    # Paso 2: Ingresar credenciales desde el CSV
    login_page.login(usuario, clave)

    # Paso 3: Validar resultado según credenciales
    if usuario == "standard_user" and clave == "secret_sauce":
        # Login exitoso → debe entrar al inventario
        assert login_page.verificar_login_exitoso()
    else:
        # Login fallido → debe mostrar mensaje de error
        assert login_page.verificar_login_fallido()
