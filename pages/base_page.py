from typing import Union

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, browser: Union[webdriver.Chrome, webdriver.Firefox], url, timeout=10):
        """
        Initializes a BasePage object.

        Args:
            browser (Union[webdriver.Chrome, webdriver.Firefox]): The web browser instance.
            url (str): The URL of the page.
            timeout (int, optional): The implicit wait timeout in seconds. Defaults to 10.
            region(Union[UralRegion, KamchatkaRegion]): Dataclass, contains variables for checking pages
        """
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        self.region = None

    def open(self):
        """Opens the specified URL in the web browser"""
        self.browser.get(self.url)

    def is_element_present(self, how, what) -> bool:
        """Checks if an element is present on the page."""
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def get_attributes(self, element) -> dict:
        """Returns the attributes of a given HTML element."""
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
        """Checks if the current URL matches the specified pattern."""
        try:
            WebDriverWait(self.browser, 3).until(EC.url_matches(url))
        except TimeoutException:
            return False
        return True

    def scroll_to_locator(self, how, what, presented=True):
        """Scrolls to the specified element on the page."""
        if not presented:
            assert self.is_element_present(how, what), \
                "There's no element"
        element = self.browser.find_element(how, what)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def element_is_clickable(self, how, what, timeout=10) -> bool:
        """Waits for an element to be clickable."""
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable((how, what))
            )
        except TimeoutException:
            return False
        return True
