from pages.sbis_main_page import SbisMainPage


def test_photos_size_first_scenario(browser):
    link = "https://sbis.ru/"
    websites = {
        "sbis_main": "https://sbis.ru/",
        "sbis_contacts": "https://sbis.ru/contacts",
        "tensor_main": "https://tensor.ru/",
        "tensor_about": "https://sbis.ru/",
    }
    page = SbisMainPage(browser, link)
    page.open()
    page.find_and_click_contacts()
    page = SbisContactsPage(browser, browser.current_url)
    page.find_and_click_tensor_banner()
    page = TensorMainPage(browser, browser.current_url)
    page.checking_the_block_power_of_man()
    page.photo_size_comparison()
