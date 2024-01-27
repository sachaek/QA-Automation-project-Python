from .base_page import BasePage


class TensorMainPage(BasePage):
    link = 'https://tensor.ru/'

    def checking_the_block_power_of_man(self):
        self.should_be_power_of_man_block()
        self.should_be_button_about()
        self.click_button_about()
        self.check_for_tensor_about_page()