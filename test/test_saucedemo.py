import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By  
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from utils.helpers import login_saucedemo, get_driver


@pytest.fixture #(scope='session')
def driver():
    #configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()


def test_login(driver ):
    login_saucedemo(driver)
    assert "/inventory.html" in driver.current_url
    titulo = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == "Products"

    
    #logueo de usuario con username y password
    #click al boton de login

    #rediriga a la pagina de inventario"

    #verificar e titulo de la pagina(Ventanita)

def test_catalogo( driver: WebDriver):
    login_saucedemo(driver)

    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    assert len(products) > 0



def test_carrito( driver: WebDriver ):
    login_saucedemo( driver )
    products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    total_products = len(products)

    products[0].find_element(By.TAG_NAME, 'button').click()

    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    assert badge == '1'

    #OTRA FORMA EVALUANDO MAS ELEMENTOS EN EL CARRITO***********
    #def test_carrito( driver: WebDriver ):
    #login_saucedemo( driver )
    #products = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    #total_products = len(products)

    #if total_products >= 2:
    #    products[0].find_element(By.TAG_NAME, 'button').click()
    #    products[1].find_element(By.TAG_NAME, 'button').click()

    #    badge = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
    #    assert badge == '2'




    #logueo de usuario con username y password
    #click al boton de login

    #podamos verificar el titulo del html

    #comprobar si existen los productos de la pagina visibles (len())
    #verificar elementos importantes de la pagina
