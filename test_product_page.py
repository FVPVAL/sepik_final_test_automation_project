import pytest
import time

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.main_page import MainPage


@pytest.mark.need_review
@pytest.mark.parametrize('offer', [1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, offer):
    """Гость может добавить продукт в корзину"""
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_match_title()
    page.should_be_the_same_price()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_by_success_present()


def test_guest_cant_see_success_message(browser):
    """Гость не видит сообщения, что товар добавлен в корзину"""
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_by_success_present()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    """Гость может видеть ссылку для входа на странице с продуктами"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """Гость может перейти на страницу авторизации со страницы с продуктами"""
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_basket_is_empty()


@pytest.mark.user_add_product
class TestUserAddToBasketFromProductPage:
    """Тесты на добавление зарегистрированным пользователем книг в корзину"""
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, "Gfhjkm13579")
        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """Пользователь может добавить продукт в корзину"""
        link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.should_be_match_title()
        page.should_be_the_same_price()

    def test_user_cant_see_success_message(self, browser):
        """Пользователь не видит сообщения, что товар добавлен в корзину"""
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_by_success_present()
