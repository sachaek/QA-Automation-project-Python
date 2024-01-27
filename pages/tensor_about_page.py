from .base_page import BasePage
from .locators import TensorAboutPageLocators


class TensorAboutPage(BasePage):
    link = 'https://tensor.ru/about'

    def photo_size_comparison(self):
        self.scroll_to_we_are_working_block()
        self.check_photo_size_attributes()

    def scroll_to_we_are_working_block(self):
        element = self.browser.find_element(*TensorAboutPageLocators.WORKING_BLOCK)
