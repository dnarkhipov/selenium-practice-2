import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.locators import ProductPageLocators


product_links_1 = [
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
]

product_links_2 = [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
]

product_links_3 = [
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
]


@pytest.mark.parametrize('link', product_links_1)
def test_guest_can_add_product_to_basket_bug(browser, link):
    page = ProductPage(browser, link)
    page.open()

    product_title = page.get_product_title()
    product_price = page.get_product_price_text()

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    # Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром,
    # который вы действительно добавили.
    basket_title_text = page.browser.find_element(*ProductPageLocators.BASKET_ALERT_TITLE).text
    assert basket_title_text == product_title, \
        'Название товара в сообщении не совпадает с тем товаром, который добавили'

    # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
    basket_price_text = page.browser.find_element(*ProductPageLocators.BASKET_ALERT_PRICE).text
    # Стоимость корзины теперь составляет <strong>9,99&nbsp;£</strong>
    assert basket_price_text.find(product_price) >= 0, 'Стоимость корзины не совпадает с ценой товара'


@pytest.mark.parametrize('link', product_links_2)
def test_guest_can_add_product_to_basket_bug(browser, link):
    page = ProductPage(browser, link)
    page.open()

    product_title = page.get_product_title()
    product_price = page.get_product_price_text()

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    # Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром,
    # который вы действительно добавили.
    basket_title_text = page.browser.find_element(*ProductPageLocators.BASKET_ALERT_TITLE).text
    assert basket_title_text == product_title, \
        'Название товара в сообщении не совпадает с тем товаром, который добавили'

    # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
    basket_price_text = page.browser.find_element(*ProductPageLocators.BASKET_ALERT_PRICE).text
    # Стоимость корзины теперь составляет <strong>9,99&nbsp;£</strong>
    assert basket_price_text.find(product_price) >= 0, 'Стоимость корзины не совпадает с ценой товара'


@pytest.mark.parametrize('link', product_links_3)
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.add_product_to_basket()
    # Проверяем, что нет сообщения об успехе
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message is presented, but should not be"


@pytest.mark.parametrize('link', product_links_3)
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    # Проверяем, что нет сообщения об успехе
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
        "Success message is presented, but should not be"


@pytest.mark.parametrize('link', product_links_3)
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.add_product_to_basket()
    # Проверяем, что нет сообщения об успехе
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()