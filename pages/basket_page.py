from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def get_items_list(self):
        return self.browser.find_element(*BasketPageLocators.BASKET_ITEMS).text

    def get_content_text(self):
        return self.browser.find_element(*BasketPageLocators.BASKET_CONTENT).text

    def should_be_empty(self):
        # Ожидаем, что в корзине нет товаров
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Items list is presented, but should not be"

        # Ожидаем, что есть текст о том что корзина пуста
        assert self.get_content_text(), "Missed text 'Your basket is empty' in Basket page"
