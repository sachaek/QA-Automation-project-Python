from .base_page import BasePage
from .locators import TensorAboutPageLocators


class TensorAboutPage(BasePage):
    link = 'https://tensor.ru/about'

    def photo_size_comparison(self):
        self.scroll_to_we_are_working_block()
        self.check_photo_size_attributes()

    def scroll_to_we_are_working_block(self):
        assert self.is_element_present(*TensorAboutPageLocators.WORKING_BLOCK), \
            "There's no <We are Working> block"
        element = self.browser.find_element(*TensorAboutPageLocators.WORKING_BLOCK)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)

    def check_photo_size_attributes(self):
        photos = self.browser.find_elements(*TensorAboutPageLocators.PHOTOS)
        for photo in photos:


