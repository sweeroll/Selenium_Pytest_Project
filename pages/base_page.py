from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, app):
        self.app = app

    def find_element(self, locator, wait_time=10):
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def find_clickable_element(self, locator, wait_time=10):
        element = WebDriverWait(self.app.driver, wait_time).until(
            EC.element_to_be_clickable(locator),
            message=f"Element not clickable {locator}",
        )
        return element

    def find_elements(self, locator):
        return self.app.driver.find_elements(*locator)

    def find_select_element(self, locator):
        select_element = Select(self.find_element(locator))
        return select_element

    def select_value(self, select_element, value):
        select_element.select_by_value(value)

    def fill_element(self, element, text):
        element.clear()
        if text:
            element.send_keys(text)
            return element

    def fill_file_input(self, file_input, file):
        file_input.clear()
        if file:
            file_input.send_keys(file)
            return file_input

    def click_element(self, element):
        element.click()

    def make_screenshot(self):
        return self.app.driver.get_screenshot_as_png()

    def execute_js(self, js_script):
        self.app.driver.execute_script(js_script)

    def get_page_url(self):
        return self.app.driver.current_url
     
    def click_enter(self, element):
        element.send_keys(Keys.RETURN)
