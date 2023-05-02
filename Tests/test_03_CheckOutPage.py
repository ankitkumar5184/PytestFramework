from Config.conf import testData
from Pages.LogOutPage import LogOutPage
from Pages.LoginPage import LoginPage
from Pages.CheckOutPage import CheckOutPage
from Tests.TestBase import BaseTest


class Test_AddToCart(BaseTest):

    def test_addToCart(self):
        self.loginPage = LoginPage(self.driver)
        self.logOutPage = LogOutPage(self.driver)
        self.checkoutPage = CheckOutPage(self.driver)
        self.loginPage.get_login_page_title()
        self.loginPage.do_login(testData.USERNAME, testData.PASSWORD)
        self.checkoutPage.add_Cart()
        self.checkoutPage.add_Data(testData.FIRSTNAME, testData.LASTNAME, testData.PINCODE)
        self.logOutPage.do_logout()
