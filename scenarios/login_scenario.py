import utils.utils as utils
from selenium.webdriver.common.by import By
import time


def test_open_app(driver):
    try:
        driver.get(utils.APP)
    except:
        utils.save_screenshot(driver, 'test_open_app')
        raise


def test_login_negative(driver):
    try:
        utils.type_text(driver, utils.USERNAME, By.NAME, utils.username_locator)
        utils.type_text(driver, utils.BAD_PASSWORD, By.NAME, utils.password_locator)
        utils.click(driver, By.XPATH, utils.login_button)
        time.sleep(3)
        assert driver.find_element(By.CSS_SELECTOR, utils.error).is_displayed()
    except:
        utils.save_screenshot(driver, 'test_login')
        raise


def test_login_positive(driver):
    try:
        utils.type_text(driver, utils.USERNAME, By.NAME, utils.username_locator)
        utils.type_text(driver, utils.PASSWORD, By.NAME, utils.password_locator)
        utils.click(driver, By.XPATH, utils.login_button)
        time.sleep(3)
        assert driver.find_element(By.CSS_SELECTOR, utils.user_menu).is_displayed()
    except:
        utils.save_screenshot(driver, 'test_login')
        raise


def test_teardown_function(driver):
    try:
        driver.close()
        driver.quit()
    except:
        utils.save_screenshot(driver, 'test_teardown')
        raise
