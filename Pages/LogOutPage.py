from Config.locators import Locator
from Pages.BasePage import BasePage


class LogOutPage(BasePage):

    def do_logout(self):
        self.do_click(Locator.OPEN_MENU_BUTTON)
        self.do_click(Locator.LOGOUT_BUTTON)
