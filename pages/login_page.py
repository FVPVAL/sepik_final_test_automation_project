from .base_page import BasePage
from .locators import LoginPageLocator


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "There is no 'login' substring in the current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocator.LOGIN_FORM), \
            "There is no login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocator.REGISTER_FORM), \
            "There is no register form"
