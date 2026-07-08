"""
InventoryPage: the product listing page shown after login.
Handles adding items to cart, sorting, and reading product data.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class InventoryPage:
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    SORT_DROPDOWN = (By.CSS_SELECTOR, ".product_sort_container")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    ITEM_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")

    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart_by_name(self, product_name):
        """
        Sauce Demo builds each 'Add to cart' button's ID from the product
        name, e.g. 'Sauce Labs Backpack' -> 'add-to-cart-sauce-labs-backpack'.
        """
        button_id = "add-to-cart-" + product_name.lower().replace(" ", "-")
        self.driver.find_element(By.ID, button_id).click()

    def get_cart_count(self):
        """Returns number shown on the cart badge, or 0 if cart is empty."""
        try:
            return int(self.driver.find_element(*self.CART_BADGE).text)
        except Exception:
            return 0

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()

    def sort_by(self, option_value):
        """
        option_value examples on saucedemo:
        'az' (Name A-Z), 'za' (Name Z-A), 'lohi' (Price low-high), 'hilo' (Price high-low)
        """
        Select(self.driver.find_element(*self.SORT_DROPDOWN)).select_by_value(option_value)

    def get_displayed_prices(self):
        """Returns list of prices (as floats) in the order currently displayed."""
        elements = self.driver.find_elements(*self.ITEM_PRICES)
        return [float(e.text.replace("$", "")) for e in elements]

    def get_displayed_names(self):
        elements = self.driver.find_elements(*self.ITEM_NAMES)
        return [e.text for e in elements]
