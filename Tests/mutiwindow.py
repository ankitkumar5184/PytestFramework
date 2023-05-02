import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_multi_window(browser):
    # Navigate to a page with a link that opens a new window
    browser.get("https://www.google.com")
    link = browser.find_element("Open new window")
    link.click()

    # Switch to the new window
    browser.switch_to.window(browser.window_handles[1])

    # Perform actions in the new window
    assert browser.title == "New window title"
    # ...

    # Close the new window and switch back to the original window
    browser.close()
    browser.switch_to.window(browser.window_handles[0])

    # Assert the expected results in the original window
    assert browser.title == "Example website"
    # ...
