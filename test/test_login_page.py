from page.login_page import LoginPage


def test_login(driver):
    #crear objeto de la pagina de login
    loginpage = LoginPage(driver)
    loginpage.open()
    loginpage.Login()
   