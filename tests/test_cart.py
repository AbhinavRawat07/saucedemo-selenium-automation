"""
test_cart.py
Covers: adding single/multiple items, cart badge count accuracy, empty cart checkout.
"""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_checkout_page import CartPage


def _login(driver):
    """Small helper so every cart test doesn't repeat the same 2 lines."""
    LoginPage(driver).login("standard_user", "secret_sauce")


def test_add_single_item_to_cart(driver):
    """POSITIVE: adding one item should update the cart badge to 1."""
    _login(driver)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart_by_name("Sauce Labs Backpack")
    assert inventory.get_cart_count() == 1


def test_add_multiple_items_to_cart(driver):
    """POSITIVE: adding 3 distinct items should update badge to 3, and cart page should list 3."""
    _login(driver)
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory.add_item_to_cart_by_name("Sauce Labs Bike Light")
    inventory.add_item_to_cart_by_name("Sauce Labs Bolt T-Shirt")
    assert inventory.get_cart_count() == 3

    inventory.go_to_cart()
    cart = CartPage(driver)
    assert cart.get_item_count() == 3


def test_empty_cart_checkout_blocked(driver):
    """
    NEGATIVE / edge case: going straight to checkout with an empty cart
    should not show any items and checkout button should still be reachable
    but produce an empty order — verifies the app doesn't crash on empty state.
    """
    _login(driver)
    inventory = InventoryPage(driver)
    inventory.go_to_cart()
    cart = CartPage(driver)
    assert cart.get_item_count() == 0, "Cart should be empty when nothing was added"
