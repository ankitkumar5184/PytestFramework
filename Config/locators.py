from selenium.webdriver.common.by import By


class Locator:
    """LoginPage Objects"""
    USERNAME = (By.XPATH, '//input[@name="user-name"]')
    PASSWORD = (By.XPATH, '//input[@name="password"]')
    loginButton = (By.XPATH, '//input[@name="login-button"]')
    """LogOutPage Objects"""
    OPEN_MENU_BUTTON = (By.XPATH, '//button[@id="react-burger-menu-btn"]')
    LOGOUT_BUTTON = (By.XPATH, '//a[@id="logout_sidebar_link"]')
    """AddProductToCartPAge Objects"""
    common_path = (By.XPATH, '(//div[@class="inventory_item_name"])[1]')
    add_to_cart = (By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory"]')
    back_to_page = (By.XPATH, '//button[@name="back-to-products"]')
    """CheckOutPage Objects"""
    CART_BUTTON = (By.XPATH, '//a[@class="shopping_cart_link"]')
    ADD_CART_BUTTON = (By.XPATH, '//button[@name="checkout"]')
    NAME_TEXT = (By.XPATH, '//input[@name="firstName"]')
    LAST_NAME_TEXT = (By.XPATH, '//input[@name="lastName"]')
    POST_CODE_TEXT = (By.XPATH, '//input[@name="postalCode"]')
    CONTINUE_BUTTON = (By.XPATH, '//input[@name="continue"]')
    FINISH_BUTTON = (By.XPATH, '//*[@id="finish"]')
    HEADER_PATH = (By.XPATH, '//h2[@class="complete-header"]')