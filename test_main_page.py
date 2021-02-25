from pages import MainPage, BasketPage, LoginPage, BasketPageLocators


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)

    # Ожидаем, что в корзине нет товаров
    assert basket_page.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
        "Items list is presented, but should not be"

    # Ожидаем, что есть текст о том что корзина пуста
    assert basket_page.get_content_text(), "Missed text 'Your basket is empty' in Basket page"
