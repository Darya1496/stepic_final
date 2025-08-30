from selenium.webdriver.common.by import By

class LoginPageLocators:
    AUTH_LINK = (By.XPATH, "//h2[text()='Войти']")
    REG_LINK = (By.XPATH, "//h2[text()='Зарегистрироваться']")

    REG_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_SUBMIT = (By.CSS_SELECTOR, "#register_form > button")

class BasePageLocators:

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:

    BASKET_LINK = (By.XPATH, "//span[@class='btn-group']/a[@class='btn btn-default']")  #Ссылка на корзину в шапке страницы
    BASKET_INFO = (By.XPATH, "//div[@id='content_inner']/p")  #Если корзина пуста
    BASKET_FULL = (By.XPATH, "//h2[text()='Товары в корзине']") #Если корзина не пустая