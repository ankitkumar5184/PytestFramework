from Config.conf import testData
from Config.locators import Locator
from Pages.BasePage import BasePage
from pytest_html_reporter import attach


class LoginPage(BasePage):
    """Constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(testData.BASE_URL)

    """Page actions"""

    def get_login_page_title(self):
        # return self.get_title(title)
        title = self.get_title()
        print('\nTitle :', title)
        assert title == "Swag Labs"

    def do_login(self, username, password):
        self.do_send_keys(Locator.USERNAME, username)
        attach(data=self.driver.get_screenshot_as_png())
        self.do_send_keys(Locator.PASSWORD, password)
        attach(data=self.driver.get_screenshot_as_png())
        self.do_click(Locator.loginButton)
        attach(data=self.driver.get_screenshot_as_png())
        title = self.get_title()
        assert title == "Swag Labs"

