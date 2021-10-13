from selenium.webdriver.remote.webelement import WebElement

from common.constants import SignUpConstants
from locators.sign_up_page_locators import SignUpLocators
from pages.base_page import BasePage
import logging

logger = logging.getLogger("moodle")


class SignUp(BasePage):
    def login_id_input(self) -> WebElement:
        return self.find_element(SignUpLocators.LOGIN_INPUT)

    def password_id_input(self) -> WebElement:
        return self.find_element(SignUpLocators.PASSWORD_INPUT)

    def email_id_input(self) -> WebElement:
        return self.find_element(SignUpLocators.EMAIL_INPUT)

    def email_id_input_2(self) -> WebElement:
        return self.find_element(SignUpLocators.EMAIL_INPUT2)

    def firstname_id_input(self) -> WebElement:
        return self.find_element(SignUpLocators.FIRSTNAME_INPUT)

    def lastname_id_input(self) -> WebElement:
        return self.find_element(SignUpLocators.LASTNAME_INPUT)

    def create_new_account_button(self) -> WebElement:
        return self.find_element(SignUpLocators.CREATE_NEW_ACCOUNT_BUTTON)

    def cant_send_email_text(self) -> WebElement:
        return self.find_element(SignUpLocators.CANT_SEND_EMAIL_TEXT)

    def continue_button(self) -> WebElement:
        return self.find_element(SignUpLocators.CONTINUE_BUTTON)

    def sign_in_button(self) -> WebElement:
        return self.find_element(SignUpLocators.SIGN_IN_BUTTON)

    def send_email_again_button(self) -> WebElement:
        return self.find_element(SignUpLocators.SEND_EMAIL_AGAIN_BUTTON)

    def sign_up(self, data):
        logger.info(
            f"Sign up with Test Data:\n"
            f"Login: {data.login}\n"
            f"Password: {data.password}\n"
            f"Firstname: {data.first_name}\n"
            f"Lastname: {data.last_name}\n"
            f"Email: {data.email}\n"
        )
        self.fill_element(self.login_id_input(), data.login)
        self.fill_element(self.password_id_input(), data.password)
        self.fill_element(self.email_id_input(), data.email)
        self.fill_element(self.email_id_input_2(), data.email)
        self.fill_element(self.firstname_id_input(), data.first_name)
        self.fill_element(self.lastname_id_input(), data.last_name)
        self.click_element(self.create_new_account_button())

    def check_account_create(self):
        self.find_element(SignUpLocators.CANT_SEND_EMAIL_TEXT)
        element = self.find_elements(SignUpLocators.CONTINUE_BUTTON)
        if len(element) > 0:
            return True
        return False

    def click_continue(self):
        return self.click_element(self.continue_button())

    def click_log_in(self):
        return self.click_element(self.sign_in_button())

    def check_new_account_log_in(self):
        self.find_element(SignUpLocators.NEED_CONFIRM_ACCOUNT_TEXT)
        element = self.find_elements(SignUpLocators.SEND_EMAIL_AGAIN_BUTTON)
        if len(element) > 0:
            return True
        return False

    def is_sign_upped(self) -> bool:
        if self.get_page_url() == SignUpConstants.SIGN_UP_PAGE_URL:
            return False
        else:
            return True
