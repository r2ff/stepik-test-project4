import selenium
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

from .base_page import BasePage


class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART).click()

    def should_be_added_to_cart(self, book_name):
        text_in_locator = self.browser.find_element(By.XPATH, "//*[@id='messages']//*[contains(@class, 'alert-success')][1]").text
        assert book_name in text_in_locator, "Название книги не совпадает"
