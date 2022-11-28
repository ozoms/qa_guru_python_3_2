import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture(scope='function')
def open_browser():
    browser.open('https://google.com/ncr')

@pytest.fixture(scope='function')
def size_browser(open_browser):
    browser.driver.set_window_size(1920, 1080)
