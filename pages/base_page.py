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
        self.region = None
        try:
            self.browser.data
        except AttributeError:
            self.browser.data = None

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what) -> bool:
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def get_attributes(self, element) -> dict:
        return self.browser.execute_script(
            """
            let attr = arguments[0].attributes;
            let items = {}; 
            for (let i = 0; i < attr.length; i++) {
                items[attr[i].name] = attr[i].value;
            }
            return items;
            """,
            element
        )

    def check_for_url_matches(self, url) -> bool:
        try:
            WebDriverWait(self.browser, 3).until(EC.url_matches(url))
        except TimeoutException:
            return False
        return True

    def scroll_to_locator(self, how, what, presented=True):
        if not presented:
            assert self.is_element_present(how, what), \
                "There's no element"
        element = self.browser.find_element(how, what)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)