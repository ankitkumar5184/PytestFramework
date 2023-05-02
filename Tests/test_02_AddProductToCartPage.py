from Config.conf import testData
from Pages.AddProductToCartPage import AddProductToCartPage
from Pages.LogOutPage import LogOutPage
from Pages.LoginPage import LoginPage
from Tests.TestBase import BaseTest


class Test_AddCart(BaseTest):

    def test_addCart(self):
        self.loginPage = LoginPage(self.driver)
        self.logOutPage = LogOutPage(self.driver)
        self.addProductToCartPage = AddProductToCartPage(self.driver)
        self.loginPage.do_login(testData.USERNAME, testData.PASSWORD)
        self.addProductToCartPage.do_add_product()
        self.logOutPage.do_logout()