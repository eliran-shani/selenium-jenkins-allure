import tests.login_tests as login


def test_open_url(driver):
    login.open_app(driver)


def test_login_negative(driver):
    login.login_negative(driver)


def test_login_positive(driver):
    login.login_positive(driver)


def test_teardown(driver):
    login.teardown_function(driver)
