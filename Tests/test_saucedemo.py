from utils.driver_setup import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By
import time


# ---------------- LOGIN TESTS ----------------

def test_login_valid_credentials():
    driver = get_driver()
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    # Assertion
    assert "inventory" in driver.current_url
    driver.quit()


def test_login_invalid_password():
    driver = get_driver()
    login = LoginPage(driver)
    login.login("standard_user", "wrong_password")

    error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Epic sadface" in error
    driver.quit()


def test_login_empty_fields():
    driver = get_driver()
    driver.find_element(By.ID, "login-button").click()

    error = driver.find_element(By.CLASS_NAME, "error-message-container").text
    assert "Username is required" in error
    driver.quit()


# ---------------- PRODUCT TESTS ----------------

def test_product_list_displayed():
    driver = get_driver()
    LoginPage(driver).login("standard_user", "secret_sauce")

    products = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(products) > 0
    driver.quit()


def test_add_product_to_cart():
    driver = get_driver()
    LoginPage(driver).login("standard_user", "secret_sauce")

    InventoryPage(driver).add_product()
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "1"
    driver.quit()


def test_remove_product_from_cart():
    driver = get_driver()
    LoginPage(driver).login("standard_user", "secret_sauce")

    InventoryPage(driver).add_product()
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

    cart_badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    assert len(cart_badges) == 0
    driver.quit()


# ---------------- CART TESTS ----------------

def test_open_cart_page():
    driver = get_driver()
    LoginPage(driver).login("standard_user", "secret_sauce")

    InventoryPage(driver).open_cart()
    assert "cart" in driver.current_url
    driver.quit()


# ---------------- CHECKOUT TESTS ----------------

def test_checkout_with_valid_details():
    driver = get_driver()
    LoginPage(driver).login("standard_user", "secret_sauce")

    InventoryPage(driver).add_product()
    InventoryPage(driver).open_cart()

    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Rahul")
    driver.find_element(By.ID, "last-name").send_keys("Jadhao")
    driver.find_element(By.ID, "postal-code").send_keys("411001")
    driver.find_element(By.ID, "continue").click()

    assert "checkout-step-two" in driver.current_url
    driver.quit()


def test_finish_order():
    driver = get_driver()
    LoginPage(driver).login("standard_user", "secret_sauce")

    InventoryPage(driver).add_product()
    InventoryPage(driver).open_cart()

    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("Rahul")
    driver.find_element(By.ID, "last-name").send_keys("Jadhao")
    driver.find_element(By.ID, "postal-code").send_keys("411001")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()

    success = driver.find_element(By.CLASS_NAME, "complete-header").text

    # ✅ FIXED ASSERTION
    assert "thank you" in success.lower()

    driver.quit()


# ---------------- LOGOUT TEST ----------------

def test_logout():
    driver = get_driver()
    LoginPage(driver).login("standard_user", "secret_sauce")

    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    driver.find_element(By.ID, "logout_sidebar_link").click()

    assert "saucedemo.com" in driver.current_url
    driver.quit()