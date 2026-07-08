# Saucedemo Automated Test Suite

Automated UI test suite for [saucedemo.com](https://www.saucedemo.com/), a demo
e-commerce site built by Sauce Labs specifically for test-automation practice.

Built with **Selenium WebDriver + Python + pytest**, following the **Page
Object Model (POM)** design pattern.

## Why Page Object Model?

Locators and page actions live in `pages/`, completely separate from test
logic in `tests/`. If the site's HTML changes, only the page file needs
updating — no test file does. This is the standard structure used in real
QA automation codebases.

## Test Coverage (14 automated test cases)

| Area | File | Cases | Type |
|---|---|---|---|
| Login | `test_login.py` | valid login, wrong password, locked-out user, empty fields | 1 positive, 3 negative |
| Cart | `test_cart.py` | add single item, add multiple items, empty cart state | 2 positive, 1 edge case |
| Checkout | `test_checkout.py` | full successful order, empty required fields, missing postal code | 1 positive, 2 negative |
| Sort/Filter | `test_search_sort.py` | price low-high, price high-low, name A-Z, name Z-A | 4 positive |

**Note on scope substitutions:** saucedemo.com doesn't have a search bar,
coupon-code field, or stock-limit feature (it's a simplified demo site), so
those original scope items are covered by equivalent negative/edge cases —
empty-field validation and locked-out-user handling serve the same purpose
of testing the app's error handling.

## Setup

```bash
pip install -r requirements.txt
```

Requires Google Chrome installed locally. `webdriver-manager` handles the
matching ChromeDriver download automatically — no manual driver setup.

## Running the tests

```bash
# Run everything
pytest

# Run one file
pytest tests/test_login.py

# Run with an HTML report
pytest --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in a browser afterward to see the pass/fail
summary — this is the report to screenshot for your portfolio/resume.

## Project Structure

```
saucedemo_test_suite/
├── conftest.py              # pytest fixture: browser setup/teardown
├── pytest.ini               # pytest configuration
├── requirements.txt
├── pages/                   # Page Object Model classes
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_checkout_page.py
└── tests/                   # actual test cases
    ├── test_login.py
    ├── test_cart.py
    ├── test_checkout.py
    └── test_search_sort.py
```

## What I learned building this

- Structuring automated tests with the Page Object Model for maintainability
- Writing both positive and negative test cases, not just happy-path
- Using pytest fixtures for reliable setup/teardown across test runs
- Generating and reading automated HTML test reports
