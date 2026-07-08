"""
CartPage + CheckoutPage: cart review and the 3-step checkout flow.
"""
from selenium.webdriver.common.by import By


class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")

    def __init__(self, driver):
        self.driver = driver

    def get_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def go_to_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()


class CheckoutStepOnePage:
    """First page of checkout: name, last name, zip code."""
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def fill_info(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.FIRST_NAME).clear()
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).clear()
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).clear()
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def get_error_message(self):
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).text
        except Exception:
            return None


class CheckoutStepTwoPage:
    """Order overview page: shows totals, has 'Finish' button."""
    FINISH_BUTTON = (By.ID, "finish")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver

    def finish_order(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def get_total_text(self):
        return self.driver.find_element(*self.TOTAL_LABEL).text


class CheckoutCompletePage:
    """Final confirmation page."""
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")

    def __init__(self, driver):
        self.driver = driver

    def get_confirmation_text(self):
        return self.driver.find_element(*self.COMPLETE_HEADER).text
