from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocator.ADD_TO_CART)
        add_to_cart_button.click()
        self.solve_quiz_and_get_code()

    def should_be_match_title(self):
        assert (self.browser.find_element(*ProductPageLocator.THE_PRODUCT_ADDED_TO_THE_CART).text ==
                self.browser.find_element(*ProductPageLocator.BOOK_TITLE).text), \
            "The name of the added book does not match the selected one"

    def should_be_the_same_price(self):
        assert (self.browser.find_element(*ProductPageLocator.THE_COST_OF_THE_CART).text ==
                self.browser.find_element(*ProductPageLocator.TOTAL_IN_THE_CART).text), \
            "The cost of the basket and everything in the basket are not equal"

