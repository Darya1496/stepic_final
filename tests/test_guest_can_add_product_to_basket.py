import time

import pytest

from pages.shop.product_page import ProductPage
from pages.main_page import MainPage
from pages.base_page import BasePage

@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                   marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_add_page(browser,link):
    #Открываем страницу товара
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = MainPage(browser, link)
    page.open()

    book = ProductPage(browser,link)
    book.tap_add_button()

    num = BasePage(browser,link)
    num.solve_quiz_and_get_code()

    as_book = ProductPage(browser,link)

    """Сравнение цен"""
    as_book.get_alert_price()
    as_book.get_product_price()
    as_book.should_be_same_price()

    print("Цены совпадают!")

    """Сравнение названий"""
    as_book.get_name()
    as_book.get_name_alert()
    as_book.should_be_same_name()
    time.sleep(10)

    print("Названия совпадают!")







