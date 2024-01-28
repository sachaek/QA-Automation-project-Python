import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import SbisDownloadLocators


class SbisDownloadPage(BasePage):
    link = "https://sbis.ru/download?tab=ereport&innerTab=ereport25"
    link_matches_main = "https://sbis.ru/download"
    link_to_download = ""

    def download_windows_sbis_plugin(self):
        self.click_to_sbis_plugin_tab()
        self.get_link_to_download()

    def click_to_sbis_plugin_tab(self):
        self.browser.find_element(*SbisDownloadLocators.SBIS_PLUGIN).click()

    def get_link_to_download(self):
        assert self.is_element_present(*SbisDownloadLocators.SBIS_WIN32_CLIENT), \
            "There's no link <SBIS_WIN32_CLIENT"
        element = self.browser.find_element(*SbisDownloadLocators.SBIS_WIN32_CLIENT)
        SbisDownloadPage.link_to_download = element.get_attribute("href")



