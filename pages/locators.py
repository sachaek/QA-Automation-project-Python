from selenium.webdriver.common.by import By


class SbisMainLocators:
    CONTACTS_HEADER = (By.CSS_SELECTOR, 'a.sbisru-Header__menu-link[href="/contacts"]')
    DOWNLOAD_SBIS_BUTTON = (By.XPATH, '//a[text()="Скачать СБИС"]')


class SbisContactsLocators:
    TENSOR_CLICKABLE_BANNER = (By.CSS_SELECTOR, 'div.mt-xm-12 > a.sbisru-Contacts__logo-tensor')
    TENSOR_BANNER = (By.CSS_SELECTOR, TENSOR_CLICKABLE_BANNER[1] + ' > img')
    REGION_NEAR_CONTACTS = (By.CSS_SELECTOR, ".sbis_ru-Region-Chooser.ml-16.ml-xm-0 > .sbis_ru-Region-Chooser__text.sbis_ru-link")
    CITY_OF_PARTNER_LIST = (By.CSS_SELECTOR, "#city-id-2")
    PARTNER_LIST_BLOCK = (By.CSS_SELECTOR, ".sbisru-Contacts-List__col")
    KAMCHATKA_BUTTON = (By.CSS_SELECTOR, 'span[title="Камчатский край"]')


class SbisDownloadLocators:
    SBIS_PLUGIN = (By.CSS_SELECTOR, 'div[data-id=plugin] > div.controls-tabButton__overlay')
    SBIS_WIN32_CLIENT = (By.CSS_SELECTOR, 'a[href*="master/win32"][href*="exe"]')
    SBIS_WIN32_CLIENT_SIZE_INFO = (By.XPATH, '//a[contains(text(), "Exe")]')



class TensorMainPageLocators:
    POWER_OF_MAN_BLOCK = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content.tensor_ru-Index__card")
    POWER_OF_MAN_BLOCK_ABOUT_BUTTON = (By.XPATH, "//a[text()='Подробнее' and @href='/about']")


class TensorAboutPageLocators:
    WORKING_BLOCK = (By.CSS_SELECTOR, ".tensor_ru-About__block-title-block +.s-Grid-container")
    PHOTOS = (By.CSS_SELECTOR, "img.tensor_ru-About__block3-image.new_lazy.loaded")
    LAST_PHOTO = (By.CSS_SELECTOR, "div > div:nth-child(4) > a > div > img.tensor_ru-About__block3-image.new_lazy.loaded")