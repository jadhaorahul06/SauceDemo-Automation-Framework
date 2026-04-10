from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_checkout(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")

    ProductPage(driver).add_product()
    ProductPage(driver).open_cart()

    CartPage(driver).checkout()

    checkout = CheckoutPage(driver)
    checkout.enter_details("Rahul", "Jadhao", "411001")
    checkout.finish_order()

    assert "Thank you" in checkout.get_success_text()