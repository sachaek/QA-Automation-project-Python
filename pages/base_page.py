from typing import Union

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser: Union[webdriver.Chrome, webdriver.Firefox], url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)