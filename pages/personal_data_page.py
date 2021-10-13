import logging

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.personal_data_page_locators import PersonalDataPageLocators, \
    PersonalDataPageMoreLocators, \
    PersonalDataPageTagLocators, \
    PersonalDataPageOptionalLocators
from pages.base_page import BasePage

logger = logging.getLogger("moodle")


class PersonalDataPage(BasePage):
    def basic_data(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.BASIC_DATA)

    def name_input(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.NAME_INPUT)

    def lastname_input(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.LASTNAME_INPUT)

    def email_input(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.EMAIL_INPUT)

    def email_display_select(self) -> WebElement:
        email_display = self.find_select_element(
            PersonalDataPageLocators.EMAIL_DISPLAY
        )
        return email_display

    def moodle_net_profile_input(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.MOODLE_NET_PROFILE)

    def city_input(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.CITY_INPUT)

    def counry_select(self) -> WebElement:
        country_select = self.find_select_element(
            PersonalDataPageLocators.COUNTRY_SELECT
        )
        return country_select

    def timezone_select(self) -> WebElement:
        country_select = self.find_select_element(
            PersonalDataPageLocators.TIMEZONE_SELECT
        )
        return country_select

    def about_input(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.ABOUT)

    def user_image_file_add_button(self) -> WebElement:
        return self.find_clickable_element(
            PersonalDataPageLocators.USER_IMAGE_FILE_ADD_BUTTON
        )

    def user_image_file_choose_input(self) -> WebElement:
        return self.find_clickable_element(
            PersonalDataPageLocators.USER_IMAGE_FILE_CHOOSE_INPUT
        )

    def download_file_button(self) -> WebElement:
        return self.find_clickable_element(
            PersonalDataPageLocators.DOWNLOAD_FILE_BUTTON
        )

    def user_image_description_input(self) -> WebElement:
        return self.find_clickable_element(
            PersonalDataPageLocators.USER_IMAGE_DESCRIPTION
        )

    def submit_button(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.SUBMIT_BUTTON)

    def input_name(self, name):
        self.fill_element(self.name_input(), name)

    def input_lastname(self, lastname):
        self.fill_element(self.lastname_input(), lastname)

    def input_email(self, email):
        self.fill_element(self.email_input(), email)

    def select_email_display(self, value):
        self.select_value(self.email_display_select(), value)

    def input_moodle_net_profile(self, url):
        self.fill_element(self.moodle_net_profile_input(), url)

    def input_city(self, city):
        self.fill_element(self.city_input(), city)

    def select_country(self, value):
        self.select_value(self.counry_select(), value)

    def select_timezone(self, value):
        self.select_value(self.timezone_select(), value)

    def input_about(self, text):
        self.fill_element(self.about_input(), text)

    def choose_user_image_file(self, image_file):
        self.click_element(self.user_image_file_add_button())
        self.fill_element(self.user_image_file_choose_input(), image_file)
        self.click_element(self.download_file_button())

    def input_user_image_description(self, text):
        self.fill_element(self.user_image_description_input(), text)

    def submit_changes(self):
        self.click_element(self.submit_button())

    def edit_personal_data(self, data):
        logger.info(
            f"Editing basic personal data with next values:\n"
            f"name: {data.name}\n"
            f"last_name: {data.last_name}\n"
            f"email: {data.email}\n"
            f"email_display_mode: {data.email_display_mode}\n"
            f"city: {data.city}\n"
            f"country_code: {data.country_code}\n"
            f"timezone: {data.timezone}\n"
            f"about: {data.about}\n"
        )
        self.input_name(data.name)
        self.input_lastname(data.last_name)
        self.input_email(data.email)
        self.select_email_display(data.email_display_mode)
        self.input_moodle_net_profile(data.moodle_net_profile)
        self.input_city(data.city)
        self.select_country(data.country_code)
        self.select_timezone(data.timezone)
        self.input_about(data.about)
        self.submit_changes()

    def is_changed(self, wait_time=10):
        header_user_info_elements = WebDriverWait(
            self.app.driver, wait_time
        ).until(
            EC.presence_of_all_elements_located(
                PersonalDataPageLocators.NAVBAR_ITEMS
            ),
            message=f"Can't find elements by locator "
                    f"{PersonalDataPageLocators.NAVBAR_ITEMS}",
        )
        if len(header_user_info_elements) == 2:
            return True
        else:
            return False

    def set_user_image(self, image_file, user_image_description):
        self.choose_user_image_file(image_file)
        self.input_user_image_description(user_image_description)
        self.submit_changes()

    def is_user_image_changed(self):
        if self.is_changed() and not self.find_elements(
                PersonalDataPageLocators.USER_PROFILE_DEFAULT_PICTURE
        ):
            return True
        else:
            return False


class PersonalDataPageMore(BasePage):

    def find_open_info(self) -> WebElement:
        return self.find_element(
            PersonalDataPageMoreLocators.MORE_SECTION_BUTTON
        )

    def open_info(self):
        self.click_element(self.find_open_info())

    def name_phonetic_input(self) -> WebElement:
        return self.find_element(PersonalDataPageMoreLocators.NAME_PHONETIC)

    def lastname_phonetic_input(self) -> WebElement:
        return self.find_element(
            PersonalDataPageMoreLocators.LAST_NAME_PHONETIC
        )

    def middle_name_input(self) -> WebElement:
        return self.find_element(PersonalDataPageMoreLocators.MIDDLE_NAME)

    def alternate_name_input(self) -> WebElement:
        return self.find_element(PersonalDataPageMoreLocators.ALTERNATE_NAME)

    def input_name_phonetic(self, name_phonetic):
        self.fill_element(self.name_phonetic_input(), name_phonetic)

    def input_lastname_phonetic(self, lastname_phonetic):
        self.fill_element(self.lastname_phonetic_input(), lastname_phonetic)

    def input_middle_name(self, middle_name):
        self.fill_element(self.middle_name_input(), middle_name)

    def input_alternate_name(self, alternate_name):
        self.fill_element(self.alternate_name_input(), alternate_name)

    def submit_button(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.SUBMIT_BUTTON)

    def submit_changes(self):
        self.click_element(self.submit_button())

    def edit_personal_data_more(self, data):
        self.open_info()
        self.input_name_phonetic(data.name_phonetic)
        self.input_lastname_phonetic(data.lastname_phonetic)
        self.input_middle_name(data.middlename)
        self.input_alternate_name(data.alternatename)
        self.submit_changes()

    def is_changed(self):
        self.find_element(PersonalDataPageMoreLocators.BODY)
        element = self.find_elements(PersonalDataPageMoreLocators.CHANGE)
        if len(element) > 0:
            return True
        return False


class PersonalDataPageOptional(BasePage):

    def find_open_info(self) -> WebElement:
        return self.find_element(
            PersonalDataPageOptionalLocators.OPTIONAL_SECTION_BUTTON
        )

    def open_info(self):
        self.click_element(self.find_open_info())

    def find_individual_number(self) -> WebElement:
        return self.find_element(
            PersonalDataPageOptionalLocators.INDIVIDUAL_NUMBER_INPUT
        )

    def individual_number_input(self, individualnumber):
        self.fill_element(self.find_individual_number(), individualnumber)

    def find_institution(self) -> WebElement:
        return self.find_element(
            PersonalDataPageOptionalLocators.INSTITUTION_INPUT
        )

    def institution_input(self, institution):
        self.fill_element(self.find_institution(), institution)

    def find_department(self) -> WebElement:
        return self.find_element(
            PersonalDataPageOptionalLocators.DEPARTMENT_INPUT
        )

    def department_input(self, department):
        self.fill_element(self.find_department(), department)

    def find_phone1(self) -> WebElement:
        return self.find_element(PersonalDataPageOptionalLocators.PHONE1_INPUT)

    def phone1_input(self, phone1):
        self.fill_element(self.find_phone1(), phone1)

    def find_phone2(self) -> WebElement:
        return self.find_element(PersonalDataPageOptionalLocators.PHONE2_INPUT)

    def phone2_input(self, phone2):
        self.fill_element(self.find_phone2(), phone2)

    def find_address(self) -> WebElement:
        return self.find_element(
            PersonalDataPageOptionalLocators.ADDRESS_INPUT
        )

    def address_input(self, address):
        self.fill_element(self.find_address(), address)

    def submit_button(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.SUBMIT_BUTTON)

    def submit_changes(self):
        self.click_element(self.submit_button())

    def edit_personal_data_optional(self, data):
        self.open_info()
        self.individual_number_input(data.individualnumber)
        self.institution_input(data.institution)
        self.department_input(data.department)
        self.phone1_input(data.phone1)
        self.phone2_input(data.phone2)
        self.address_input(data.address)
        self.submit_changes()

    def is_changed(self):
        self.find_element(PersonalDataPageMoreLocators.BODY)
        element = self.find_elements(PersonalDataPageMoreLocators.CHANGE)
        if len(element) > 0:
            return True
        return False


class PersonalDataPageTag(BasePage):

    def find_open_info(self) -> WebElement:
        return self.find_element(
            PersonalDataPageTagLocators.TAG_SECTION_BUTTON
        )

    def open_info(self):
        self.click_element(self.find_open_info())

    def find_tag(self) -> WebElement:
        return self.find_element(PersonalDataPageTagLocators.TAG_INPUT)

    def tag_input(self, tag):
        self.fill_element(self.find_tag(), tag)
        self.click_enter(self.find_tag())

    def submit_button(self) -> WebElement:
        return self.find_element(PersonalDataPageLocators.SUBMIT_BUTTON)

    def submit_changes(self):
        self.click_element(self.submit_button())

    def edit_personal_data_tag(self, data):
        self.open_info()
        self.tag_input(data.tag)
        self.submit_changes()

    def is_changed(self):
        self.find_element(PersonalDataPageMoreLocators.BODY)
        element = self.find_elements(PersonalDataPageMoreLocators.CHANGE)
        if len(element) > 0:
            return True
        return False
