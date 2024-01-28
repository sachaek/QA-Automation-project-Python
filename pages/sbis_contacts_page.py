import time

from .sbis_contacts_regions import UralRegion, KamchatkaRegion
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

    def check_for_ural_region(self):
        self.region = UralRegion()
        self.check_for_region()
        self.region = None
        self.should_be_partners_list()

    def check_for_region(self):
        self.should_be_my_region_near_contacts()
        self.should_be_main_city_of_region_in_the_top_of_partners()
        self.should_be_my_region_in_current_url()

    def should_be_my_region_in_current_url(self):
        assert self.region.MY_REGION_SUBSTRING in self.browser.current_url, \
            f"Expacted url contains: {self.region.MY_REGION_SUBSTRING}, current url: {self.browser.current_url}"

    def should_be_my_region_near_contacts(self):
        assert self.is_element_present(*SbisContactsLocators.REGION_NEAR_CONTACTS), \
            "There's no name of region, near the contacs"
        assert self.check_for_url_matches(self.region.MY_REGION_SUBSTRING)
        assert self.region.MY_REGION_NAME_RUS in self.browser.find_element(*SbisContactsLocators.REGION_NEAR_CONTACTS).text, \
            "Not <MY_REGION_NAME_RUS> in text, "\
            f"Should be <{self.region.MY_REGION_NAME_RUS}>" \
            f", current: <{self.browser.find_element(*SbisContactsLocators.REGION_NEAR_CONTACTS).text}>"

    def should_be_main_city_of_region_in_the_top_of_partners(self):
        assert self.is_element_present(*SbisContactsLocators.CITY_OF_PARTNER_LIST), \
            "There's no name of region, near the partner list"
        assert self.region.MAIN_CITY_OF_MY_REGION in self.browser.find_element(*SbisContactsLocators.CITY_OF_PARTNER_LIST).text,\
            "WRONG MAIN CITY NAME in text, in top of partner list"

    def should_be_partners_list(self):
        assert self.is_element_present(*SbisContactsLocators.PARTNER_LIST_BLOCK)

    def change_to_Kamchatka_region(self):
        self.region = KamchatkaRegion()
        self.click_to_region_text()
        self.click_to_kamchatka_text()
        self.check_for_region()
        self.should_be_partners_list()
        self.region = None

    def click_to_region_text(self):
        self.browser.find_element(*SbisContactsLocators.REGION_NEAR_CONTACTS).click()

    def click_to_kamchatka_text(self):
        assert self.is_element_present(*SbisContactsLocators.KAMCHATKA_BUTTON), \
            "There's no Kamchatka Button"
        self.browser.find_element(*SbisContactsLocators.KAMCHATKA_BUTTON).click()






