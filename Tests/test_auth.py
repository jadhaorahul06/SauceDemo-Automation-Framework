from pages.login_page import LoginPage

def test_login_valid(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

def test_login_invalid(driver):
    LoginPage(driver).login("wrong", "wrong")
    assert "error" in driver.page_source