from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product(self):
        self.driver.find_element(By.CLASS_NAME, "btn_inventory").click()

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()