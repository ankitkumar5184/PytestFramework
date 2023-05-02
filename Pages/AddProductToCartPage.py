from Pages.BasePage import BasePage
from Config.locators import Locator


class AddProductToCartPage(BasePage):

    def do_add_product(self):
        self.do_click(Locator.common_path)
        self.do_click(Locator.add_to_cart)
        self.do_click(Locator.back_to_page)
