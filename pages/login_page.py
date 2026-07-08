"""
LoginPage: represents the saucedemo.com login screen.
This file ONLY knows about locators and low-level actions on this page.
It does NOT contain any assertions — that's the test's job.
"""
from selenium.webdriver.common.by import By


class LoginPage:
    # --- Locators (found via browser DevTools -> Inspect Element) ---
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        """Fills the login form and submits it."""
        self.driver.find_element(*self.USERNAME_INPUT).clear()
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def get_error_message(self):
        """Returns the error text shown on failed login, or None if absent."""
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).text
        except Exception:
            return None
