import time
from .base_page import BasePage
from .locators import SbisDownloadLocators


class SbisDownloadPage(BasePage):
    """
    Represents the Sbis Download page with specific methods for downloading the Windows Sbis plugin.

    Attributes:
        link (str): The URL of the Sbis Download page.
        link_matches_main (str): The URL that should match the main Download page.
        link_to_download (str): The link to download the Windows Sbis plugin.
        file_size (str): The size of the downloaded file.

    Methods:
        download_windows_sbis_plugin(): Initiates the download process for the Windows Sbis plugin.
        click_to_sbis_plugin_tab(): Clicks on the eReport tab to access the Sbis plugin section.
        get_link_to_download(): Retrieves the link to download the Windows Sbis plugin.
        get_file_size(): Retrieves the file size information from the Download page.
    """
    link = "https://sbis.ru/download?tab=ereport&innerTab=ereport25"
    link_matches_main = "https://sbis.ru/download"
    link_to_download = ""
    file_size = ""

    def download_windows_sbis_plugin(self):
        """Initiates the download process for the Windows Sbis plugin."""
        self.click_to_sbis_plugin_tab()
        self.get_link_to_download()
        self.get_file_size()

    def click_to_sbis_plugin_tab(self):
        """Clicks on the eReport tab to access the Sbis plugin section."""
        self.browser.find_element(*SbisDownloadLocators.SBIS_PLUGIN).click()

    def get_link_to_download(self):
        """
        Retrieves the link to download the Windows Sbis plugin.

        Raises:
        AssertionError: If the current URL does not match the expected pattern for the plugin page.
        """
        assert self.check_for_url_matches("tab=plugin"), \
            "It's not a plugin page"
        element = self.browser.find_element(*SbisDownloadLocators.SBIS_WIN32_CLIENT)
        SbisDownloadPage.link_to_download = element.get_attribute("href")

    def get_file_size(self):
        """
        Retrieves the file size information from the Download page.

        Raises:
        AssertionError: If there is no file size information on the page.
        """
        assert self.is_element_present(*SbisDownloadLocators.SBIS_WIN32_CLIENT_SIZE_INFO), \
            "There's no file size, check locator"
        element = self.browser.find_element(*SbisDownloadLocators.SBIS_WIN32_CLIENT_SIZE_INFO)
        SbisDownloadPage.file_size = element.text.split()[2]
