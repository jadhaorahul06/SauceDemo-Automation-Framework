from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_add_to_cart(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    ProductPage(driver).add_product()
    ProductPage(driver).open_cart()
    assert "Your Cart" in driver.page_source