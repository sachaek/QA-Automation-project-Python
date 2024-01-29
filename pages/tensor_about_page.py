import time

from .base_page import BasePage
from .locators import TensorAboutPageLocators


class TensorAboutPage(BasePage):
    """
    Represents the Tensor About page with specific methods for photo size comparison.

    Attributes:
        link (str): The URL of the Tensor About page.

    Methods:
        photo_size_comparison(): Scrolls to the "We are Working" block and checks photo size attributes.
        scroll_to_we_are_working_block(): Scrolls to the "We are Working" block on the page.
        check_photo_size_attributes(): Checks the size attributes of the photos on the page.
    """
    link = 'https://tensor.ru/about'

    def photo_size_comparison(self):
        self.scroll_to_we_are_working_block()
        self.check_photo_size_attributes()

    def scroll_to_we_are_working_block(self):
        assert self.is_element_present(*TensorAboutPageLocators.WORKING_BLOCK), \
            "There's no <We are Working> block"
        self.scroll_to_locator(*TensorAboutPageLocators.WORKING_BLOCK)

    def check_photo_size_attributes(self):
        """
        Checks the size attributes of the photos on the page.

        Raises:
            AssertionError: If any of the photo sizes do not match the expected size (270x192).
        """

        self.browser.find_element(*TensorAboutPageLocators.LAST_PHOTO) # wait for load images
        photos = self.browser.find_elements(*TensorAboutPageLocators.PHOTOS)
        count = 0
        for photo in photos:
            count += (photo.get_attribute('width') == '270')
            count += (photo.get_attribute('height') == '192')
        assert count == 8, \
            f"One of photo sizes are not expected (Expected: 270x192)"