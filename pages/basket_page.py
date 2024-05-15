from .base_page import BasePage
from .locators import BasketPageLocator


class BasketPage(BasePage):
    """Корзина"""
    def should_not_be_product_in_basket(self):
        """В корзине не должно быть товара"""
        assert self.is_not_element_present(*BasketPageLocator.PRODUCT_IN_BASKET), \
        "There are items in the basket, but they should not be"

    def should_be_basket_is_empty(self):
        """В корзине должен быть текст, что корзина пуста"""
        assert self.is_element_present(*BasketPageLocator.BASKET_IS_EMPTY), \
        "There is no message that the trash is empty"
