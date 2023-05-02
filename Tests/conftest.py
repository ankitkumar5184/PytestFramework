import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
        web_driver.maximize_window()
        web_driver.implicitly_wait(10)
        web_driver.delete_all_cookies()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
        web_driver.maximize_window()
        web_driver.implicitly_wait(10)
        web_driver.delete_all_cookies()
    if request.param == "edge":
        web_driver = webdriver.Edge()
        web_driver.maximize_window()
        web_driver.implicitly_wait(10)
        web_driver.delete_all_cookies()
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    yield
    web_driver.close()
