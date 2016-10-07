import tests.tests as tests


# Test step 1 - Open URL
def test_open_url(driver, url):
    tests.open_url(driver, url)


# Test step 2 - Add credentials
def test_add_credentials(driver, username, password):
    tests.add_credentials(driver, username, password)


# Test step 3 - Submit form
def test_submit_form(driver):
    tests.submit_form(driver)


# Test step 4 - verify URL
def test_verify_url(driver, url):
    tests.verify_url(driver, url)
