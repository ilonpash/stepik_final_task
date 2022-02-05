from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS),\
            "Items in the basket are presented, but should not be"

    def should_be_empty_basket_message_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT),\
            "Empty basket message text in the basket are not presented, but should be"

