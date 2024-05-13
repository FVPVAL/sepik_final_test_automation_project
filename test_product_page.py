import pytest

from .pages.product_page import ProductPage


@pytest.mark.parametrize('offer', [1, 2, 3, 4, 5, 6, pytest.param(7, marks=pytest.mark.xfail), 8, 9])
def test_guest_can_add_product_to_basket(browser, offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_be_match_title()
    page.should_be_the_same_price()
