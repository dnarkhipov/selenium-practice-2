from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def get_product_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text

    def get_product_price_text(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_product_to_basket(self):
        product_title = self.get_product_title()
        product_price = self.get_product_price_text()

        self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET).click()
        self.solve_quiz_and_get_code()

        # Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром,
        # который вы действительно добавили.
        basket_title_text = self.browser.find_element(*ProductPageLocators.BASKET_ALERT_TITLE).text
        assert basket_title_text == product_title, \
            'Название товара в сообщении не совпадает с тем товаром, который добавили'

        # Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        basket_price_text = self.browser.find_element(*ProductPageLocators.BASKET_ALERT_PRICE).text
        # Стоимость корзины теперь составляет <strong>9,99&nbsp;£</strong>
        assert basket_price_text.find(product_price) >= 0, 'Стоимость корзины не совпадает с ценой товара'
