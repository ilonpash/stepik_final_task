from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def text_of_book_name(self):
        name_of_book = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT)
        return name_of_book.text

    def text_of_book_price(self):
        price_of_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT)
        return price_of_book.text

    def should_be_same_name(self, name_of_book):
        # name_of_book = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        name_in_message = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_MESS).text
        assert name_in_message == name_of_book, f"Incorrect Product was added to the basket - {name_in_message} is not {name_of_book}"

    def should_be_same_price(self, price_of_book):
        # price_of_book = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        price_in_message = self.browser.find_element(*ProductPageLocators.PRICE_OF_PRODUCT_MESS).text
        assert price_in_message == price_of_book, f"Incorrect Price in the basket - {price_in_message} is not {price_of_book}"