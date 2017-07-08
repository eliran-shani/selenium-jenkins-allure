import pytest
from selenium.webdriver.common.by import By

APP = "https://demo.moodle.net/"
USERNAME = "admin"
PASSWORD = "sandbox"
BAD_PASSWORD = "1234"

# Locators
username_locator = "username"
password_locator = "password"
login_button = "//input[@value='Log in']"
user_menu = ".usermenu"
error = '.error'
username_el = "username"
password_el = "password"
submit = "//input[@type='submit']"
expected_url = "my/"


def add_field(driver, value, field):
    username_field = driver.find_element(By.NAME, field)
    username_field.clear()
    username_field.send_keys(value)


def add_credentials(driver, username, password):
    add_field(driver, username, username_el)
    add_field(driver, password, password_el)


def submit_form(driver):
    driver.find_element(By.XPATH, submit).click()


def verify_url(driver, url):
    assert (url + expected_url) == driver.current_url


# Test step 1 - Open URL
def test_open_url(driver, url):
    driver.get(url)
    page_title = "BlazeDemo"
    driver.find_element(By.ID, page_title)
    assert driver.title == "BlazeDemo"


# Test step 2 - Add credentials
def test_add_credentials(driver, username, password):
    add_credentials(driver, username, password)


# Test step 3 - Submit form
def test_submit_form(driver):
    submit_form(driver)


# Test step 4 - verify URL
def test_verify_url(driver, url):
    verify_url(driver, url)
