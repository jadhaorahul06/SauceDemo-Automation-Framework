from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time


def test_valid_login():
    driver = get_driver()
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    time.sleep(2)
    driver.quit()


def test_invalid_login():
    driver = get_driver()
    login = LoginPage(driver)
    login.login("standard_user", "wrong_password")
    time.sleep(2)
    driver.quit()


def test_add_to_cart():
    driver = get_driver()
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_product()
    time.sleep(2)
    driver.quit()


def test_open_cart():
    driver = get_driver()
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.open_cart()
    time.sleep(2)
    driver.quit()