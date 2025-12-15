import pytest
from page.login_page import LoginPage
from data.data_login import CASOS_LOGIN
from utils.example_csv import get_login_csv

@pytest.mark.parametrize("username, password, login_bool", CASOS_LOGIN)
def test_login(driver, username, password, login_bool):
    #crear objeto de la pagina de login
    loginpage = LoginPage(driver)
    loginpage.open()
    loginpage.Login(username, password)
   