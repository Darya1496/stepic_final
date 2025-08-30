from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Страница входа не открылась"
        assert True

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.AUTH_LINK), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REG_LINK), "Registration form is not presented"
        assert True

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        password_field.send_keys(password)

        password_field2 = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_REPEAT)
        password_field2.send_keys(password)

        submit = self.browser.find_element(*LoginPageLocators.REG_SUBMIT)
        submit.click()

