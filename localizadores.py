from selenium.webdriver.common.by import By

class SwagLabsLocators:
    enter_username = (By.XPATH, '//*[@id="user-name"]')
    enter_password = (By.XPATH, '//*[@id="password"]')
    loggin_button = (By.CSS_SELECTOR, '#login-button')
    add_backpack = (By.ID, 'add-to-cart-sauce-labs-backpack')
    add_saucelabs = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    click_shoppingcar = (By.CLASS_NAME, 'shopping_cart_link')
    remove_backpack = (By.XPATH, '//*[@id="remove-sauce-labs-backpack"]')

