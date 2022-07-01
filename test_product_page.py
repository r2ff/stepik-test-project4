import time

from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    book_name = "Coders at Work"
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_added_to_cart(book_name)
    # time.sleep(60)