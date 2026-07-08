"""
test_search_sort.py
Covers: sorting products by price (low-high, high-low) and by name (A-Z, Z-A).
Note: saucedemo.com has no search bar, so 'search' from the original scope
is covered via sorting/filtering instead -- see README for this substitution.
"""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def _login(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")


def test_sort_price_low_to_high(driver):
    """POSITIVE: prices should be in ascending order after sorting."""
    _login(driver)
    inventory = InventoryPage(driver)
    inventory.sort_by("lohi")
    prices = inventory.get_displayed_prices()
    assert prices == sorted(prices), f"Prices not ascending: {prices}"


def test_sort_price_high_to_low(driver):
    """POSITIVE: prices should be in descending order after sorting."""
    _login(driver)
    inventory = InventoryPage(driver)
    inventory.sort_by("hilo")
    prices = inventory.get_displayed_prices()
    assert prices == sorted(prices, reverse=True), f"Prices not descending: {prices}"


def test_sort_name_a_to_z(driver):
    """POSITIVE: product names should be alphabetically ascending."""
    _login(driver)
    inventory = InventoryPage(driver)
    inventory.sort_by("az")
    names = inventory.get_displayed_names()
    assert names == sorted(names), f"Names not A-Z: {names}"


def test_sort_name_z_to_a(driver):
    """POSITIVE: product names should be alphabetically descending."""
    _login(driver)
    inventory = InventoryPage(driver)
    inventory.sort_by("za")
    names = inventory.get_displayed_names()
    assert names == sorted(names, reverse=True), f"Names not Z-A: {names}"
