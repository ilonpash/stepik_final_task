from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, 'p.price_color')
    NAME_OF_PRODUCT_MESS = (By.CSS_SELECTOR, 'div.alertinner > strong')
    PRICE_OF_PRODUCT_MESS = (By.CSS_SELECTOR, '.alertinner p strong')
