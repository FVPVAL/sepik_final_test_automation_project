from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_linc_in")


class MainPageLocators:
    pass


class LoginPageLocator:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocator:
    ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    THE_PRODUCT_ADDED_TO_THE_CART = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > .alertinner  > strong")
    THE_COST_OF_THE_CART = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > .alertinner  > p > strong")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    TOTAL_IN_THE_CART = (By.CSS_SELECTOR, ".product_main > p:nth-child(2)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
