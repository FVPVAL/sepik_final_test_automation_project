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

    def register_new_user(self, email, password):
        register_mail = self.browser.find_element(*LoginPageLocator.REGISTER_MAIL)
        register_mail.send_keys(email)
        register_password = self.browser.find_element(*LoginPageLocator.REGISTER_PASSWORD)
        register_password.send_keys(password)
        register_repeat_password = self.browser.find_element(*LoginPageLocator.REGISTER_REPEAT_PASSWORD)
        register_repeat_password.send_keys(password)
        btn_register = self.browser.find_element(*LoginPageLocator.BTN_REGISTER)
        btn_register.click()
