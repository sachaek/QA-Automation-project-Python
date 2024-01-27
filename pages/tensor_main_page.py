from .base_page import BasePage
from .locators import TensorMainPageLocators


class TensorMainPage(BasePage):
    link = 'https://tensor.ru/'

    def checking_the_block_power_of_man(self):
        self.should_be_power_of_man_block()
        self.should_be_button_about()
        self.click_button_about()
        self.check_for_tensor_about_page()

    def should_be_power_of_man_block(self):
        assert self.is_element_present(*TensorMainPageLocators.POWER_OF_MAN_BLOCK)

    def should_be_button_about(self):
        assert self.is_element_present(*TensorMainPageLocators.POWER_OF_MAN_BLOCK_ABOUT_BUTTON)

    def click_button_about(self):
        element = self.browser.find_element(*TensorMainPageLocators.POWER_OF_MAN_BLOCK_ABOUT_BUTTON)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def check_for_tensor_about_page(self):
        new_window = self.browser.window_handles[-1]
        self.browser.switch_to.window(new_window)
        assert TensorMainPage.link == self.browser.current_url, \
            f"current page are not tensor.ru, current page : {self.browser.current_url}