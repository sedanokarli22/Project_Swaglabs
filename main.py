from selenium import webdriver
import data
import localizadores
import metodos
from metodos import SwagLabsPage
from localizadores import SwagLabsLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import swags_labs, username


class TestSwagLabs:
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.locators_page = SwagLabsPage(cls.driver)

# PROCESO DE AGREGAR A LA CESTA DOS ARTICULOS
   # 1.- INICIO DE SESION
    def test_loggin(self):
     self.driver.get(data.swags_labs)
     locators_page = SwagLabsPage(self.driver)
     self.driver.implicitly_wait(30)
     username = data.username
     password = data.password
     locators_page.set_loggin(username, password)
     locators_page.click_loggin()
     assert locators_page.get_user() == username
     assert locators_page.get_password() == password

    # 2.- SELECCIONA DOS ARTICULOS DE LA TIENDA
 #   def test_select_inventory(self):
 #       self.driver.get(data.swags_labs)
 #       locators_page = SwagLabsPage(self.driver)
  #      self.driver.implicitly_wait(30)
#        locators_page.select_backpack()
 #       locators_page.select_saucelabs()

    #3.- SELECCIONA EL CARRITO DE COMPRA
#    def test_select_shoppingcar(self):
   #     self.driver.get(data.swags_labs)
 #       locators_page = SwagLabsPage(self.driver)
  #      self.driver.implicitly_wait(10)
 #       locators_page.select_shoppingcar()

    #4.- ELIMINA UN ARTICULO DEL CARRITO DE COMPRA
#    def test_delete_backpack(self):
#        self.driver.get(data.swags_labs)
 #       locators_page = SwagLabsPage(self.driver)
#        self.driver.implicitly_wait(5)
  #      locators_page.remove_backpack()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()











