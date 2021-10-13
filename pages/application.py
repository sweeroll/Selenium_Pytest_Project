from pages.login_page import LoginPage
from pages.personal_data_page import PersonalDataPage, PersonalDataPageMore, \
    PersonalDataPageOptional, PersonalDataPageTag
from pages.sign_up_page import SignUp


class Application:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.login = LoginPage(self)
        self.personal_data = PersonalDataPage(self)
        self.sign_up = SignUp(self)
        self.personal_data_more = PersonalDataPageMore(self)
        self.personal_data_optional = PersonalDataPageOptional(self)
        self.personal_data_tag = PersonalDataPageTag(self)

    def open_main_page(self):
        self.driver.get(self.url)

    def quit(self):
        self.driver.quit()

    def open_auth_page(self):
        self.driver.get(self.url + "/login/index.php")
