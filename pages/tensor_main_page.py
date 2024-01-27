from .base_page import BasePage
from .locators import TensorMainPageLocators
from .tensor_about_page import TensorAboutPage


class TensorMainPage(BasePage):
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
        new_window = self.browser.window_handles[-1]
        self.browser.switch_to.window(new_window)
        assert TensorAboutPage.link == self.browser.current_url, \
            f"current page are not TensorAboutPage, current page : {self.browser.current_url}"
