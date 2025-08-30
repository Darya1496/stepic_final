from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class BasketPage(BasePage):
    BASKET_LINK = (By.XPATH, "//span[@class='btn-group']/a[@class='btn btn-default']")  #Ссылка на корзину в шапке страницы
    BASKET_INFO = (By.XPATH, "//div[@id='content_inner']/p")  #Если корзина пуста
    BASKET_FULL = (By.XPATH, "//h2[text()='Товары в корзине']") #Если корзина не пустая

    """Переход на страницу корзины"""
    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasketPage.BASKET_LINK)
        basket_link.click()
        return BasketPage(browser=self.browser, url=self.browser.current_url)

    def get_text_busket(self):
        """Получаем текст из описания корзины"""
        name_alert_element = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(BasketPage.BASKET_INFO))
        return name_alert_element.text.strip()

    def should_be_same_text(self):
        """Сравниваем текст в корзине с ожидаемым"""
        info = self.get_text_busket()
        text = "Ваша корзина пуста Продолжить покупки"

        assert info == text, \
            f"Корзина не пуста!\n" \
            f"Ожидается: {info}\n" \
            f"В сообщении: {text}"

    def should_not_be_product_message(self):
        assert self.is_not_element_present(*BasketPage.BASKET_FULL), \
            "В корзине присутствуют товары, ожидается пустая корзина"