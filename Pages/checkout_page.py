from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_details(self, fname, lname, zip):
        self.driver.find_element(By.ID, "first-name").send_keys(fname)
        self.driver.find_element(By.ID, "last-name").send_keys(lname)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip)
        self.driver.find_element(By.ID, "continue").click()

    def finish_order(self):
        self.driver.find_element(By.ID, "finish").click()

    def get_success_text(self):
        return self.driver.find_element(By.CLASS_NAME, "complete-header").text