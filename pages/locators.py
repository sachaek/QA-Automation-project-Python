from selenium.webdriver.common.by import By


class SbisMainLocators:
    CONTACTS_HEADER = (By.CSS_SELECTOR, 'a.sbisru-Header__menu-link[href="/contacts"]')


class SbisContactsLocators:
    TENSOR_CLICKABLE_BANNER = (By.CSS_SELECTOR, 'div.mt-xm-12 > a.sbisru-Contacts__logo-tensor')
    TENSOR_BANNER = (By.CSS_SELECTOR, TENSOR_CLICKABLE_BANNER[1] + ' > img')
    TO_MAIN_TENSOR = (By.CSS_SELECTOR, ".tensor_ru")