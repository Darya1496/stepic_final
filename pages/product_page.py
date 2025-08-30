from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators_product_page import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):

    def tap_add_button(self):
        """Нажимаем кнопку Добавить в корзину"""
        add = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add.click()


    def get_product_price(self):
        """Получаем текст цены со страницы товара"""
        price_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.PRICE_PRODUCT))
        return price_element.text.strip()

    def get_alert_price(self):
        """Получаем текст цены из сообщения (например, в корзине)"""
        alert_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.PRICE_ALLERT))
        return alert_element.text.strip()

    def should_be_same_price(self):
        """Сравниваем цены"""
        product_price = self.get_product_price()
        alert_price = self.get_alert_price()

        assert product_price == alert_price, \
            f"Цена в корзине не соответствует цене товара!\n" \
            f"На странице: {product_price}\n" \
            f"В сообщении: {alert_price}"

    def get_name(self):
        """Получаем текст названия со страницы товара"""
        name_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.NAME_BOOK_ON_PAGE))
        return name_element.text.strip()

    def get_name_alert(self):
        """Получаем текст названия из сообщения (например, в корзине)"""
        name_alert_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(ProductPageLocators.NAME_ADD_BOOK))
        return name_alert_element.text.strip()

    def should_be_same_name(self):
        """Сравниваем названия"""
        product_name = self.get_name()
        alert_name = self.get_name_alert()

        assert product_name == alert_name, \
            f"Название в корзине не соответствует названию товара!\n" \
            f"На странице: {product_name}\n" \
            f"В сообщении: {alert_name}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCSESS_ADD_BOOK), \
            "Success message is presented, but should not be"


    def should_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCSESS_ADD_BOOK), \
            "Success message is presented, but should be disappeared"