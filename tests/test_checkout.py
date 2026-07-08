"""
test_checkout.py
Covers: full successful checkout, and empty required-field validation
(this stands in for the 'invalid coupon code' style negative case, since
saucedemo doesn't have a coupon field -- see README for the substitution note).
"""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_checkout_page import (
    CartPage, CheckoutStepOnePage, CheckoutStepTwoPage, CheckoutCompletePage
)


def _login_and_add_item(driver):
    LoginPage(driver).login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    inventory.add_item_to_cart_by_name("Sauce Labs Backpack")
    inventory.go_to_cart()


def test_full_checkout_flow_success(driver):
    """POSITIVE: complete happy-path checkout should reach the confirmation page."""
    _login_and_add_item(driver)
    CartPage(driver).go_to_checkout()

    step_one = CheckoutStepOnePage(driver)
    step_one.fill_info("Abhinav", "Rawat", "248001")

    step_two = CheckoutStepTwoPage(driver)
    step_two.finish_order()

    complete = CheckoutCompletePage(driver)
    assert "thank you" in complete.get_confirmation_text().lower()


def test_checkout_empty_required_fields(driver):
    """NEGATIVE: submitting checkout step 1 with no info should show a validation error."""
    _login_and_add_item(driver)
    CartPage(driver).go_to_checkout()

    step_one = CheckoutStepOnePage(driver)
    step_one.fill_info("", "", "")
    error = step_one.get_error_message()
    assert error is not None
    assert "first name is required" in error.lower()


def test_checkout_missing_postal_code(driver):
    """NEGATIVE: filling name but leaving postal code empty should still error."""
    _login_and_add_item(driver)
    CartPage(driver).go_to_checkout()

    step_one = CheckoutStepOnePage(driver)
    step_one.fill_info("Abhinav", "Rawat", "")
    error = step_one.get_error_message()
    assert error is not None
    assert "postal code is required" in error.lower()
