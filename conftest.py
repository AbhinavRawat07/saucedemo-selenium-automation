"""
conftest.py holds shared pytest fixtures.
"""
import pytest
from selenium import webdriver

BASE_URL = "https://www.saucedemo.com/"


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    chrome_driver = webdriver.Chrome(options=options)
    chrome_driver.get(BASE_URL)

    yield chrome_driver

    chrome_driver.quit()