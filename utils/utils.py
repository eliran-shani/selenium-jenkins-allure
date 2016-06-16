import moment
import os
import string

# Constants
now = moment.now().strftime("%d-%m-%Y")
path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
screen_dir = os.path.join(path, "screenshot", str(now))

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

# Functions
def screen_path():
    global screen_dir
    if not os.path.exists(screen_dir):
        os.makedirs(screen_dir)
        os.chmod(screen_dir, 0755)
    return screen_dir


def save_screenshot(driver, name):
    _name = remove_special_characters(name)
    driver.get_screenshot_as_file(os.path.join(screen_path(), _name + '-' + now + ".png"))


def remove_special_characters(text):
    return text.translate(string.maketrans('', ''), '\ / : * ? " < > |')


def click(driver, *args):
    el = driver.find_element(*args)
    el.click()


def type_text(driver, text, *args):
    el = driver.find_element(*args)
    el.click()
    el.send_keys(text)
