from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url.find('login') >= 0, "URL of the current page is invalid"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*MainPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(*MainPageLocators.REGISTER_FORM), "Register form is not presented"
