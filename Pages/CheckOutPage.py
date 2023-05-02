from Config.locators import Locator
from Pages.BasePage import BasePage


class CheckOutPage(BasePage):

    def add_Cart(self):
        self.do_click(Locator.CART_BUTTON)
        self.do_click(Locator.ADD_CART_BUTTON)

    def add_Data(self, firstName, lastName, pinCode):
        self.do_send_keys(Locator.NAME_TEXT, firstName)
        self.do_send_keys(Locator.LAST_NAME_TEXT, lastName)
        self.do_send_keys(Locator.POST_CODE_TEXT, pinCode)
        self.do_click(Locator.CONTINUE_BUTTON)
        self.do_click(Locator.FINISH_BUTTON)
        text = self.get_element_text(Locator.HEADER_PATH)
        print("\nText :" + text)
        assert text == "Thank you for your order!"


