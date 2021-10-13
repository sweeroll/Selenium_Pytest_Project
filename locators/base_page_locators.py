from selenium.webdriver.common.by import By


class BasePageLocators:
    SIGN_IN = (By.CLASS_NAME, "header_user_info")
    HEADER_USER_INFO = (By.CLASS_NAME, "header_user_info")
    CONFIRM_EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")
