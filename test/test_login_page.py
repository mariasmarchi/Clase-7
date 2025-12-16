import pytest
import csv
from page.login_page import LoginPage

# Función para leer el CSV
def leer_datos_csv(path):
    with open(path, newline='') as f:
        return [(row["username"], row["password"]) for row in csv.DictReader(f)]

# Parametrización usando data_login.csv
@pytest.mark.parametrize("usuario,clave", leer_datos_csv("data/data_login.csv"))
def test_login_parametrizado(driver, usuario, clave):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(usuario, clave)  # usa tu método actual con mayúscula

    if usuario == "standard_user" and clave == "secret_sauce":
        # Caso positivo: debería entrar al inventario
        assert "inventory" in driver.current_url
    else:
        # Caso negativo: debería mostrar mensaje de error
        assert login_page.mensaje_error_visible()
