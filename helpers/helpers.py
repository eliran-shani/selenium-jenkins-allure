import moment
import os
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Constants
now = moment.now().strftime("%d-%m-%Y")
path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
screen_dir = os.path.join(path, "screenshot", str(now))


def screen_path():
    global screen_dir
    if not os.path.exists(screen_dir):
        os.makedirs(screen_dir)
        os.chmod(screen_dir, 0755)
    return screen_dir


def remove_special_characters(text):
    return text.translate(string.maketrans('', ''), '\ / : * ? " < > |')


def save_screenshot(driver, name):
    _name = remove_special_characters(name)
    driver.get_screenshot_as_file(os.path.join(screen_path(), _name + '-' + now + ".png"))


def click(driver, by_type, locator):
    el = driver.find_element(by_type, locator)
    el.click()


def type_text(driver, text, by_type, locator):
    el = driver.find_element(by_type, locator)
    el.click()
    el.send_keys(text)


def wait_for_page_load(driver, by_type, locator):
    delay = 3  # seconds
    try:
        myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((by_type, locator)))
        print "Page is ready!"
    except TimeoutException:
        print "Loading took too much time!"
