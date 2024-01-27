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


