import pytest

from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link_on_product_page(self,browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """Гость открывает главную страницу """
    link = "http://selenium1py.pythonanywhere.com"
    page = BasePage(browser, link)
    page.open()

    """Переходим на страницу корзины"""
    bas = BasketPage(browser, link)
    bas.go_to_basket_page()

    """Ожидаем, что в корзине нет товаров"""
    bas.should_not_be_product_message()

    """Ожидаем, что есть текст о том что корзина пуста """
    bas.get_text_busket()
    bas.should_be_same_text()
