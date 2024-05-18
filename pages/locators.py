from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_linc_in")
    VIEW_BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocator:
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "h2.col-sm-6")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p:nth-child(1)")


class LoginPageLocator:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_MAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    BTN_REGISTER = (By.CSS_SELECTOR, "#register_form > button")


class MainPageLocators:
    pass


class ProductPageLocator:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    THE_PRODUCT_ADDED_TO_THE_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > .alertinner  > strong")
    THE_COST_OF_THE_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > .alertinner  > p > strong")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main > h1")
    TOTAL_IN_THE_BASKET = (By.CSS_SELECTOR, ".product_main > p:nth-child(2)")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
