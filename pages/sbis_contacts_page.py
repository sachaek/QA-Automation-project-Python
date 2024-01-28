import time

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
        new_window = self.browser.window_handles[-1]
        self.browser.switch_to.window(new_window)
        assert TensorMainPage.link == self.browser.current_url, \
            f"current page are not tensor.ru, current page : {self.browser.current_url}"

    def check_for_region(self):
        self.should_be_my_region_in_current_url()
        self.should_be_my_region_near_contacts()
        self.should_be_main_city_of_region_in_the_top_of_partners()
        self.should_be_partners_list()

    def should_be_my_region_in_current_url(self):
        MY_REGION_SUBSTRING = "66-sverdlovskaya-oblast"
        assert MY_REGION_SUBSTRING in self.browser.current_url

    def should_be_my_region_near_contacts(self):
        MY_REGION_NAME_RUS = "Свердловская"
        assert self.is_element_present(*SbisContactsLocators.REGION_NEAR_CONTACTS), \
            "There's no name of region, near the contacs"
        assert MY_REGION_NAME_RUS in self.browser.find_element(*SbisContactsLocators.REGION_NEAR_CONTACTS).text, \
            "Not <MY_REGION_NAME_RUS> in text"

    def should_be_main_city_of_region_in_the_top_of_partners(self):
        MAIN_CITY_OF_MY_REGION = "Екатеринбург"
        assert self.is_element_present(*SbisContactsLocators.CITY_OF_PARTNER_LIST), \
            "There's no name of region, near the partner list"
        assert MAIN_CITY_OF_MY_REGION in self.browser.find_element(*SbisContactsLocators.CITY_OF_PARTNER_LIST),\
            "WRONG MAIN CITY NAME in text, in top of partner list"

    def should_be_partners_list(self):
        assert self.is_element_present(*SbisContactsLocators.PARTNER_LIST_BLOCK)

