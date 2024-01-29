import pytest

from .local_machine.my_computer import MyComputer
from .pages.tensor_about_page import TensorAboutPage
from .pages.tensor_main_page import TensorMainPage
from .pages.sbis_contacts_page import SbisContactsPage
from .pages.sbis_main_page import SbisMainPage
from .pages.sbis_download_page import SbisDownloadPage


def test_photos_size_first_scenario(browser):
    page = SbisMainPage(browser, SbisMainPage.link)
    page.open()
    page.find_and_click_contacts()
    page = SbisContactsPage(browser, browser.current_url)
    page.find_and_click_tensor_banner()
    page = TensorMainPage(browser, browser.current_url)
    page.checking_the_block_power_of_man()
    page = TensorAboutPage(browser, browser.current_url)
    page.photo_size_comparison()


def test_change_to_kamchatka_second_scenario(browser):
    page = SbisMainPage(browser, SbisMainPage.link)
    page.open()
    page.find_and_click_contacts()
    page = SbisContactsPage(browser, browser.current_url)
    page.check_for_ural_region()
    page.change_to_Kamchatka_region()


def test_download_file_sbis_third_scenario(browser):
    page = SbisMainPage(browser, SbisMainPage.link)
    page.open()
    page.find_and_click_download_sbis()
    page = SbisDownloadPage(browser, browser.current_url)
    page.download_windows_sbis_plugin()
    my_pc = MyComputer(SbisDownloadPage.link_to_download, SbisDownloadPage.file_size)
    my_pc.check_file_in_project()