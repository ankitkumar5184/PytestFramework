from Config.conf import testData
from Pages.LogOutPage import LogOutPage
from Pages.LoginPage import LoginPage
from Tests.TestBase import BaseTest


class Test_Login(BaseTest):

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.logOutPage = LogOutPage(self.driver)
        self.loginPage.do_login(testData.USERNAME, testData.PASSWORD)
        self.logOutPage.do_logout()
