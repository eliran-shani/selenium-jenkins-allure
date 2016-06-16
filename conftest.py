import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--driver", action="store", default="chrome", help="Type in browser type (chrome / firefox) ")
    parser.addoption("--username", action="store", default="admin", help="username")
    parser.addoption("--password", action="store", default="sandbox", help="password")


@pytest.fixture(scope="module", autouse=True)
def driver(request):
    browser = request.config.getoption("--driver")
    if browser == 'chrome':
        browser = webdriver.Chrome()
        browser.get("about:blank")
        browser.implicitly_wait(10)
        browser.set_window_size(1680, 1050)
        browser.set_window_position(0, 0)
        # browser.maximize()
        return browser
    elif browser == 'firefox':
        browser = webdriver.Firefox()
        browser.get("about:blank")
        browser.implicitly_wait(10)
        browser.set_window_size(1680, 1050)
        browser.set_window_position(0, 0)
        # browser.maximize()
        return browser


@pytest.fixture(scope="module")
def username(request):
    return request.config.getoption("--username")


@pytest.fixture(scope="module")
def password(request):
    return request.config.getoption("--password")
