import time
import pytest

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.base_page import BasePage
from pages.basket_page import BasketPage


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    """Открываем страницу товара """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = BasePage(browser, link)
    page.open()

    book = ProductPage(browser,link)
    book.tap_add_button()

    page.solve_quiz_and_get_code()

    as_book = ProductPage(browser,link)

    """Сравнение цен"""
    as_book.get_alert_price()
    as_book.get_product_price()
    as_book.should_be_same_price()

    """Сравнение названий"""
    as_book.get_name()
    as_book.get_name_alert()
    as_book.should_be_same_name()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Открываем страницу товара """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasePage(browser, link, timeout=0)
    page.open()

    """Добавляем товар в корзину """
    book = ProductPage(browser,link,timeout=0)
    book.tap_add_button()

    """Проверяем, что нет сообщения об успехе с помощью is_not_element_present"""
    book.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    """Открываем страницу товара """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasePage(browser, link, timeout=0)
    page.open()

    """Добавляем товар в корзину """
    book = ProductPage(browser,link,timeout=0)
    book.tap_add_button()

    """Проверяем, что нет сообщения об успехе с помощью is_not_element_present"""
    book.should_disappeared_message()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """Гость открывает страницу товара"""
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
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

@pytest.mark.registration
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = BasePage(browser,link)
        page.open()

        email = str(time.time()) + "@fakemail.org"
        password = "qwezxcasd"

        reg = LoginPage(browser, link) #Регистрация нового пользователя
        reg.register_new_user(email, password)

        page.should_be_authorized_user()  #Проверка, что пользователь авторизован

    def test_user_cant_see_success_message_after_adding_product_to_basket(self,browser):
        """Открываем страницу товара """
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = BasePage(browser, link, timeout=0)
        page.open()

        """Добавляем товар в корзину """
        book = ProductPage(browser, link, timeout=0)
        book.tap_add_button()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """Открываем страницу товара """
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = BasePage(browser, link)
        page.open()

        book = ProductPage(browser, link)
        book.tap_add_button()

        #page.solve_quiz_and_get_code()

        as_book = ProductPage(browser, link)

        """Сравнение цен"""
        as_book.get_alert_price()
        as_book.get_product_price()
        as_book.should_be_same_price()

        """Сравнение названий"""
        as_book.get_name()
        as_book.get_name_alert()
        as_book.should_be_same_name()

