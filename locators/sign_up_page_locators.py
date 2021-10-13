from selenium.webdriver.common.by import By


class SignUpLocators:
    LOGIN_INPUT = (By.ID, "id_username")
    PASSWORD_INPUT = (By.ID, "id_password")
    EMAIL_INPUT = (By.ID, "id_email")
    EMAIL_INPUT2 = (By.ID, "id_email2")
    FIRSTNAME_INPUT = (By.ID, "id_firstname")
    LASTNAME_INPUT = (By.ID, "id_lastname")
    CREATE_NEW_ACCOUNT_BUTTON = (By.ID, "id_submitbutton")
    CANT_SEND_EMAIL_TEXT = (By.CLASS_NAME, "errormessage")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "button[id*='single_button']")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, ".login > a")
    SEND_EMAIL_AGAIN_BUTTON = (By.CSS_SELECTOR, "button[id*='single_button']")
    NEED_CONFIRM_ACCOUNT_TEXT = (By.TAG_NAME, "h2")
