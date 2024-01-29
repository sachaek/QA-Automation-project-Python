from .base_page import BasePage
from .locators import TensorMainPageLocators
from .tensor_about_page import TensorAboutPage


class TensorMainPage(BasePage):
    """
    Represents the Tensor Main page with specific methods for checking the Power of Man block.

    Attributes:
        link (str): The URL of the Tensor Main page.

    Methods:
        checking_the_block_power_of_man(): Checks the Power of Man block, clicks the ABOUT button, and checks for
        the Tensor About page.
        should_be_power_of_man_block(): Asserts the presence of the Power of Man block on the page.
        should_be_button_about(): Asserts the presence of the ABOUT button in the Power of Man block.
        click_button_about(): Clicks the ABOUT button and scrolls to the element.
        check_for_tensor_about_page(): Checks if the current page is the Tensor About page.
        """
    link = 'https://tensor.ru/'

    def checking_the_block_power_of_man(self):
        self.should_be_power_of_man_block()
        self.should_be_button_about()
        self.click_button_about()
        self.check_for_tensor_about_page()

    def should_be_power_of_man_block(self):
        assert self.is_element_present(*TensorMainPageLocators.POWER_OF_MAN_BLOCK), \
            "There's no <POWER OF MAN> block "

    def should_be_button_about(self):
        assert self.is_element_present(*TensorMainPageLocators.POWER_OF_MAN_BLOCK_ABOUT_BUTTON), \
            "There's no ABOUT button in <POWER OF MAN> block "

    def click_button_about(self):
        element = self.browser.find_element(*TensorMainPageLocators.POWER_OF_MAN_BLOCK)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        self.browser.find_element(*TensorMainPageLocators.POWER_OF_MAN_BLOCK_ABOUT_BUTTON).click()

    def check_for_tensor_about_page(self):
        """
           Checks if the current page is the Tensor About page.

           Raises:
               AssertionError: If the current page is not the Tensor About page.
        """
        new_window = self.browser.window_handles[-1]
        self.browser.switch_to.window(new_window)
        assert TensorAboutPage.link == self.browser.current_url, \
            f"current page are not TensorAboutPage, current page : {self.browser.current_url}"
