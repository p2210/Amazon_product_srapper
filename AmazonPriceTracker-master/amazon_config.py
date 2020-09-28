from selenium import webdriver

DIRECTORY = 'reports'
NAME = 'xbox'
CURRENCY = '€'
MIN_PRICE = '10'
MAX_PRICE = '78'
FILTERS = {
    'min': MIN_PRICE,
    'max': MAX_PRICE
}
BASE_URL = "http://www.amazon.de/"


def get_chrome_web_driver(options):
    return webdriver.Chrome("C:\\Users\\user\\Desktop\\Desktop2\\chromedriver_win32\\chromedriver.exe", chrome_options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')


def set_browser_as_incognito(options):
    options.add_argument('--incognito')


def set_automation_as_head_less(options):
    options.add_argument('--headless')
