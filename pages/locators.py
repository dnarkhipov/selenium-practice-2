from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//a[text()="View basket"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alert-success')


class LoginPageLocators:
    INPUT_EMAIL = (By.ID, 'id_registration-email')
    INPUT_PASSWORD_1 = (By.ID, 'id_registration-password1')
    INPUT_PASSWORD_2 = (By.ID, 'id_registration-password2')
    REG_BUTTON = (By.NAME, 'registration_submit')


class MainPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main p.price_color')
    BASKET_ALERT_TITLE = (By.CSS_SELECTOR, '#messages .alert-success .alertinner strong')
    BASKET_ALERT_PRICE = (By.CSS_SELECTOR, '#messages .alert-info .alertinner p')


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_CONTENT = (By.CSS_SELECTOR, '.content p')
