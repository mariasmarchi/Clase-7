
selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import URL, USERNAME, PASSWORD



class PersonalLoginPage:

    #USERNAME= 'standard_user'
    #PASSWORD= 'secret_sauce'
    _INPUT_NAME = 'user-name'
    _INPUT_PASSWORD = 'password'
    _LOGIN_BUTTON = 'login-button'

    def __init__(self, driver):
        self.driver = driver
    
    def oper( self)
        self.driver.get(URL)

    def Login(self, username = USERNAME, password = PASSWORD):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable( self._INPUT_NAME)       #valida si existe
        ).send_keys(username)                                   #Lo envia
        
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable( self._INPUT_PASSWORD)   #valida si existe
        ).send_keys(password)                                   #Lo envia

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable( self._LOGIN_BUTTON)    #valida si existe
        ).click()  

      

        self.driver.find_element(By.NAME, self._INPUT_PASSWORD).send_keys(password)
        self.driver.find_element(By.ID, self._LOGIN_BUTTON).click()
        