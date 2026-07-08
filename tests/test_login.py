"""
test_login.py
Covers: valid login, invalid password, locked-out user, empty fields.
Mix of POSITIVE (should succeed) and NEGATIVE (should fail gracefully) cases.
"""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage


def test_login_valid_credentials(driver):
    """POSITIVE: correct username/password should land on the inventory page."""
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert "inventory.html" in driver.current_url, "Should redirect to inventory page after valid login"


def test_login_invalid_password(driver):
    """NEGATIVE: wrong password should show an error and NOT navigate away."""
    login_page = LoginPage(driver)
    login_page.login("standard_user", "wrong_password")
    error = login_page.get_error_message()
    assert error is not None, "Expected an error message for invalid password"
    assert "do not match" in error.lower() or "epic sadface" in error.lower()
    assert "inventory.html" not in driver.current_url


def test_login_locked_out_user(driver):
    """NEGATIVE: saucedemo provides a 'locked_out_user' specifically to test this case."""
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")
    error = login_page.get_error_message()
    assert error is not None
    assert "locked out" in error.lower()


def test_login_empty_fields(driver):
    """NEGATIVE: submitting with no username/password should show a required-field error."""
    login_page = LoginPage(driver)
    login_page.login("", "")
    error = login_page.get_error_message()
    assert error is not None
    assert "username is required" in error.lower()
