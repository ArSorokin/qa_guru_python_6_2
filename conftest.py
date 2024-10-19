import pytest
from selene import browser


@pytest.fixture(scope="session", autouse=True)
def browser_select():
    browser.config.driver_name = 'firefox'
    print('Браузер стартует')
    yield
    print('Браузер закрывается')


@pytest.fixture(scope="module")
def browser_set_size(browser_select):
    browser.config.window_width = 1920
    browser.config.window_height = 1080


@pytest.fixture()
def browser_open():
    browser.open('https://google.com')
