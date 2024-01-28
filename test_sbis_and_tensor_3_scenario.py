from .pages.tensor_about_page import TensorAboutPage
from .pages.tensor_main_page import TensorMainPage
from .pages.sbis_contacts_page import SbisContactsPage
from .pages.sbis_main_page import SbisMainPage


# def test_photos_size_first_scenario(browser):
#     page = SbisMainPage(browser, SbisMainPage.link)
#     page.open()
#     page.find_and_click_contacts()
#     page = SbisContactsPage(browser, browser.current_url)
#     page.find_and_click_tensor_banner()
#     page = TensorMainPage(browser, browser.current_url)
#     page.checking_the_block_power_of_man()
#     page = TensorAboutPage(browser, browser.current_url)
#     page.photo_size_comparison()


def test_change_to_kamchatka_second_scenario(browser):
    page = SbisMainPage(browser, SbisMainPage.link)
    page.open()
    page.find_and_click_contacts()
    page = SbisContactsPage(browser, browser.current_url)
    page.check_for_Ural_region()
    page.change_to_Kamchatka_region()
