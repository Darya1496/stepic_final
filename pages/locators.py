from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    AUTH_LINK = (By.XPATH, "//h2[text()='Войти']")
    REG_LINK = (By.XPATH, "//h2[text()='Зарегистрироваться']")