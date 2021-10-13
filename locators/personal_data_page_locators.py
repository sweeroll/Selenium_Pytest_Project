from selenium.webdriver.common.by import By


class PersonalDataPageLocators:
    EDIT_INFO = (By.CSS_SELECTOR, "a[href*='editadvanced']")
    BASIC_DATA = (By.ID, "id_moodle")
    NAME_INPUT = (By.ID, "id_firstname")
    LASTNAME_INPUT = (By.ID, "id_lastname")
    EMAIL_INPUT = (By.ID, "id_email")
    MOODLE_NET_PROFILE = (By.ID, "id_moodlenetprofile")
    CITY_INPUT = (By.ID, "id_city")
    ABOUT = (By.ID, "id_description_editoreditable")
    SUBMIT_BUTTON = (By.ID, "id_submitbutton")
    NAVBAR_ITEMS = (By.CLASS_NAME, "breadcrumb-item")
    SUCCESS_ALERT = (By.CLASS_NAME, "alert-success")
    COUNTRY_SELECT = (By.ID, "id_country")
    TIMEZONE_SELECT = (By.ID, "id_timezone")
    EMAIL_DISPLAY = (By.ID, "id_maildisplay")


class PersonalDataPageMoreLocators:
    MORE_SECTION_BUTTON = (By.XPATH, "//*[text()='Дополнительная информация об имени']")
    NAME_PHONETIC = (By.ID, "id_firstnamephonetic")
    LAST_NAME_PHONETIC = (By.ID, "id_lastnamephonetic")
    MIDDLE_NAME = (By.ID, "id_middlename")
    ALTERNATE_NAME = (By.ID, "id_alternatename")
    BODY = (By.ID, "region-main-box")
    CHANGE = (By.CLASS_NAME, "alert-success")


class PersonalDataPageOptionalLocators:
    OPTIONAL_SECTION_BUTTON = (By.XPATH, "//*[text()='Необязательное']")
    INDIVIDUAL_NUMBER_INPUT = (By.ID, "id_idnumber")
    INSTITUTION_INPUT = (By.ID, "id_institution")
    DEPARTMENT_INPUT = (By.ID, "id_department")
    PHONE1_INPUT = (By.ID, "id_phone1")
    PHONE2_INPUT = (By.ID, "id_phone2")
    ADDRESS_INPUT = (By.ID, "id_address")


class PersonalDataPageTagLocators:
    TAG_SECTION_BUTTON = (By.XPATH, "//*[text()='Интересы']")
    TAG_INPUT = (By.CSS_SELECTOR, "input[placeholder='Введите теги...']")
    USER_IMAGE_DESCRIPTION = (By.ID, "id_imagealt")
    USER_IMAGE_FILE_ADD_BUTTON = (By.CLASS_NAME, "fp-btn-add")
    USER_IMAGE_FILE_CHOOSE_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    DOWNLOAD_FILE_BUTTON = (By.CLASS_NAME, "fp-upload-btn")
    USER_PROFILE_DEFAULT_PICTURE = (By.CLASS_NAME, "defaultuserpic")
