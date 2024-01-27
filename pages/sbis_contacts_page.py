from .base_page import BasePage
from .locators import SbisContactsLocators
from .tensor_main_page import TensorMainPage


class SbisContactsPage(BasePage):
    link = 'https://sbis.ru/'

    def find_and_click_tensor_banner(self):
        self.should_be_tensor_banner()
        self.click_banner()
        self.check_for_tensor_page()

    def should_be_tensor_banner(self):
        assert self.is_element_present(*SbisContactsLocators.TENSOR_BANNER), \
            f'No banner, TENSOR_BANNER={SbisContactsLocators.TENSOR_BANNER}'

    def click_banner(self):
        self.browser.find_element(*SbisContactsLocators.TENSOR_CLICKABLE_BANNER).click()

    def check_for_tensor_page(self):
        assert self.is_element_present(*SbisContactsLocators.TO_MAIN_TENSOR)
        assert  TensorMainPage.link == self.browser.current_url, \
            f"current page are not tensor.ru, current page : {self.browser.current_url}"
