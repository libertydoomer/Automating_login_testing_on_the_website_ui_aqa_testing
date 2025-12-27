from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage
from pages.locators import login_locators as loc


class UserLogin(BasePage):
    def open_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def check_current_url_is(self, expected_url):
        assert self.driver.current_url == expected_url

    def check_page_elements_are_visible(self):
        assert self.find(loc.username_field_loc).is_displayed()
        assert self.find(loc.password_field_loc).is_displayed()
        assert self.find(loc.button_loc).is_displayed()

    def fill_login_form(self, username, password):
        username_field = self.find(loc.username_field_loc)
        password_field = self.find(loc.password_field_loc)
        button = self.find(loc.button_loc)
        username_field.send_keys(username)
        password_field.send_keys(password)
        button.click()

    def check_products_title_text_is(self, text):
        WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(loc.products_title_loc)
        )
        products_title = self.find(loc.products_title_loc)
        assert products_title.text == text

    def check_error_alert_text_is(self, text):
        error_alert = self.find(loc.error_alert_loc)
        assert error_alert.text == text