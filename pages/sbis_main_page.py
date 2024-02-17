from .base_page import BasePage
from .locators import SbisMainLocators
from .sbis_contacts_page import SbisContactsPage
from .sbis_download_page import SbisDownloadPage


class SbisMainPage(BasePage):
    """
    Represents the Sbis Main page with specific methods for interaction.

    Attributes:
        link (str): The URL of the Sbis Main page.

    Methods:
        find_and_click_contacts(): Finds and clicks the Contacts header, checking for the Contacts page afterward.
        should_be_contacts_header(): Asserts the presence of the Contacts header on the page.
        click_contacts(): Clicks on the Contacts header.
        check_for_current_page(link, strict=True): Checks if the current page matches the specified link.
        find_and_click_download_sbis(): Finds and clicks the Download SBIS button, checking for the Download page
        afterward.
    """
    link = 'https://sbis.ru/'

    def find_and_click_contacts(self):
        self.should_be_contacts_header()
        self.click_contacts()
        self.check_for_url_matches(SbisContactsPage.link)
        self.check_for_current_page(SbisContactsPage.link, strict=False)

    def should_be_contacts_header(self):
        assert self.is_element_present(*SbisMainLocators.CONTACTS_HEADER)

    def click_contacts(self):
        self.browser.find_element(*SbisMainLocators.CONTACTS_HEADER).click()

    def check_for_current_page(self, link, strict=True):
        """
        Checks if the current page matches the specified link.

        Args:
            link (str): The expected link of the page.
            strict (bool, optional): If True, performs an exact match; if False, checks if the link is present
             in the current URL.

        Raises:
            AssertionError: If the current page does not match the expected link.
        """
        if strict:
            assert link == self.browser.current_url, \
                f"current page is not <{link}>, it's: <{self.browser.current_url}>"
        else:
            assert link in self.browser.current_url, \
                f"current page not matches <{link}>, it's: <{self.browser.current_url}>"

    def find_and_click_download_sbis(self):
        assert self.is_element_present(*SbisMainLocators.DOWNLOAD_SBIS_BUTTON), \
            "There's no <DOWNLOAD SBIS> button"
        self.scroll_to_locator(*SbisMainLocators.DOWNLOAD_SBIS_BUTTON)
        self.browser.find_element(*SbisMainLocators.DOWNLOAD_SBIS_BUTTON).click()
        self.check_for_current_page(SbisDownloadPage.link_matches_main, strict=False)
