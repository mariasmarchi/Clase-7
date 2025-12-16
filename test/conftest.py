import pytest
import os
from utils.helpers import get_driver

@pytest.fixture
def driver():
    # Configuración para inicializar Selenium WebDriver
    driver = get_driver()
    yield driver
    driver.quit()

# Hook para capturas automáticas en caso de fallo
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            carpeta = "reporte"
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)

            nombre_test = item.name
            ruta = os.path.join(carpeta, f"{nombre_test}.png")
            driver.save_screenshot(ruta)

            # Adjuntar la captura al reporte HTML
            if "pytest_html" in item.config.pluginmanager.list_name_plugin():
                extra = getattr(rep, "extra", [])
                rep.extra = extra + [pytest_html.extras.image(ruta)]
            print(f"\n📸 Screenshot guardado en: {ruta}")

# Hook para agregar metadata al reporte HTML
def pytest_configure(config):
    config._metadata["Proyecto"] = "EntregaSELENIUM"
    config._metadata["Autor"] = "Maria Smarchi"
