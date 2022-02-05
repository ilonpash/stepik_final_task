from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    EMAIL_REG = (By.CSS_SELECTOR, "[name='registration-email']")
    PASSWORD_REG = (By.CSS_SELECTOR, "[name='registration-password1']")
    CONFIRM_PASSWORD_REG = (By.CSS_SELECTOR, "[name='registration-password2']")
    REG_SUBMIT_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_OF_PRODUCT = (By.CSS_SELECTOR, 'p.price_color')
    NAME_OF_PRODUCT_MESS = (By.CSS_SELECTOR, 'div.alertinner > strong')
    PRICE_OF_PRODUCT_MESS = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success')


class BasketPageLocators():
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

