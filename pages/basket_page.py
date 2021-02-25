from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def get_items_list(self):
        return self.browser.find_element(*BasketPageLocators.BASKET_ITEMS).text

    def get_content_text(self):
        return self.browser.find_element(*BasketPageLocators.BASKET_CONTENT).text
