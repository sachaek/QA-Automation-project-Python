from .base_page import BasePage
from .locators import TensorMainLocators
from .sbis_contacts_page import SbisContactsPage


class SbisMainPage(BasePage):
    link = 'https://sbis.ru/'

    def find_and_click_contacts(self):
        self.should_be_contacts_header()
        self.click_contacts()
        self.check_for_current_page()

    def should_be_contacts_header(self):
        assert self.is_element_present(*TensorMainLocators.CONTACTS_HEADER)

    def click_contacts(self):
        self.browser.find_element(*TensorMainLocators.CONTACTS_HEADER).click()

    def check_for_current_page(self):
        assert self.browser.current_url == SbisContactsPage.link