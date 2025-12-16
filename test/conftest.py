import pytest
import os
from utils.helpers import get_driver
import pytest_html

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
            if hasattr(rep, "extra"):
                rep.extra.append(pytest_html.extras.image(ruta))
            else:
                rep.extra = [pytest_html.extras.image(ruta)]

            print(f"\n📸 Screenshot guardado en: {ruta}")

# Personalizar título y metadata del reporte HTML
def pytest_html_report_title(report):
    report.title = "Reporte de pruebas - EntregaSELENIUM"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([f"Proyecto: EntregaSELENIUM", f"Autor: Maria Smarchi"])
