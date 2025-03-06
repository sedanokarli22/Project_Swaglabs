from selenium import webdriver
import data
import localizadores
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



from data import username, password
from localizadores import SwagLabsLocators

class SwagLabsPage:
    def __init__(self,driver):
        self.driver = driver
        self.locators = SwagLabsLocators

    def set_user(self, intro_username):
        self.driver.find_element(*self.locators.enter_username).send_keys(username)
    def set_password(self, intro_password):
        self.driver.find_element(*self.locators.enter_password).send_keys(password)
    def get_user(self):
        self.driver.implicitly_wait(20)
        return self.driver.find_element(*self.locators.enter_username).get_property('value')
    def get_password(self):
        return self.driver.find_element(*self.locators.enter_password).get_property('value')
    def click_loggin(self):
        self.driver.implicitly_wait(15)
        self.driver.find_element(*self.locators.loggin_button).click()

    def set_loggin(self,intro_username,intro_password):
        self.driver.implicitly_wait(30)
        self.set_user(intro_username)
        self.set_password(intro_password)

    def select_backpack(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.locators.add_backpack).click()
    def select_saucelabs(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.locators.add_saucelabs).click()
    def select_shoppingcar(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.locators.click_shoppingcar).click()
    def remove_backpack(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*self.locators.remove_backpack).click()






