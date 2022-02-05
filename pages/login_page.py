from selenium import webdriver
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators
import time


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_form = self.browser.find_element(*MainPageLocators.EMAIL_REG)
        pass_form = self.browser.find_element(*MainPageLocators.PASSWORD_REG)
        pass_form_conf = self.browser.find_element(*MainPageLocators.CONFIRM_PASSWORD_REG)
        email_form.send_keys(email)
        pass_form.send_keys(password)
        pass_form_conf.send_keys(password)
        reg_confirm = self.browser.find_element(*MainPageLocators.REG_SUBMIT_BUTTON)
        reg_confirm.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This is not the login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
