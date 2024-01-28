from .base_page import BasePage
from .locators import SbisMainLocators
from .sbis_contacts_page import SbisContactsPage
from .sbis_download_page import SbisDownloadPage


class SbisMainPage(BasePage):
    link = 'https://sbis.ru/'

    def find_and_click_contacts(self):
        self.should_be_contacts_header()
        self.click_contacts()
        self.check_for_current_page(self.link)

    def should_be_contacts_header(self):
        assert self.is_element_present(*SbisMainLocators.CONTACTS_HEADER)

    def click_contacts(self):
        self.browser.find_element(*SbisMainLocators.CONTACTS_HEADER).click()

    def check_for_current_page(self, link, strict=True):
        if strict:
            assert SbisContactsPage.link == self.browser.current_url, \
                f"current page is not <{link}>, it's: <{self.browser.current_url}>"
        else:
            assert SbisContactsPage.link in self.browser.current_url, \
                f"current page not matches <{link}>, it's: <{self.browser.current_url}>"

    def find_and_click_download_sbis(self):
        assert self.is_element_present(*SbisMainLocators.DOWNLOAD_SBIS_BUTTON), \
            "There's no <DOWNLOAD SBIS> button"
        self.scroll_to_locator(*SbisMainLocators.DOWNLOAD_SBIS_BUTTON)
        self.browser.find_element(*SbisMainLocators.DOWNLOAD_SBIS_BUTTON).click()
        self.check_for_current_page(SbisDownloadPage, strict=False)
