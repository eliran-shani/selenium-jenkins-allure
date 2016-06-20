import utils.utils as utils
from selenium.webdriver.common.by import By
import time
import inspect
import pytest
import allure
import moment
from allure.constants import AttachmentType

now = moment.now().strftime("%d-%m-%Y")


def open_app(driver):
    try:
        driver.get(utils.APP)
    except:
        # Add screenshot to Allure report
        allure.attach(inspect.currentframe().f_code.co_name + "-" + now, driver.get_screenshot_as_png(),
                      type=AttachmentType.PNG)
        # Save screenshot locally
        utils.save_screenshot(driver, inspect.currentframe().f_code.co_name)
        raise


def login_negative(driver):
    try:
        utils.type_text(driver, utils.USERNAME, By.NAME, utils.username_locator)
        utils.type_text(driver, utils.BAD_PASSWORD, By.NAME, utils.password_locator)
        utils.click(driver, By.XPATH, utils.login_button)
        time.sleep(3)
        assert driver.find_element(By.CSS_SELECTOR, utils.error).is_displayed()
    except:
        # Add screenshot to Allure report
        allure.attach(inspect.currentframe().f_code.co_name + "-" + now, driver.get_screenshot_as_png(),
                      type=AttachmentType.PNG)
        # Save screenshot locally
        utils.save_screenshot(driver, inspect.currentframe().f_code.co_name)
        raise


def login_positive(driver):
    try:
        utils.type_text(driver, utils.USERNAME, By.NAME, utils.username_locator)
        utils.type_text(driver, utils.PASSWORD, By.NAME, utils.password_locator)
        utils.click(driver, By.XPATH, utils.login_button)
        time.sleep(3)
        assert driver.find_element(By.CSS_SELECTOR, utils.user_menu).is_displayed()
    except:
        # Add screenshot to Allure report
        allure.attach(inspect.currentframe().f_code.co_name + "-" + now, driver.get_screenshot_as_png(),
                      type=AttachmentType.PNG)
        # Save screenshot locally
        utils.save_screenshot(driver, inspect.currentframe().f_code.co_name)
        raise


def teardown_function(driver):
    try:
        driver.close()
        driver.quit()
    except:
        # Add screenshot to Allure report
        allure.attach(inspect.currentframe().f_code.co_name + "-" + now, driver.get_screenshot_as_png(),
                      type=AttachmentType.PNG)
        # Save screenshot locally
        utils.save_screenshot(driver, inspect.currentframe().f_code.co_name)
        raise
