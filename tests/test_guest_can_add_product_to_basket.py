import time
from pages.shop.product_page import ProductPage
from pages.main_page import MainPage
from pages.base_page import BasePage

def test_add_page(browser):
    #Открываем страницу товара
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
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

    print("Названия совпадают!")







