from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
import pytest
import time


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):  # гость может добавить товар в корзину
#     # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     product_page = ProductPage(browser, link)
#     product_page.open()
#     product_page.adding_an_product_to_basket()  # добавление товара в корзину
#     product_page.solve_quiz_and_get_code()  # подсчет математического выражения в alert
#     product_page.check_product_name_in_message()  # проверка название товара в сообщении
#     product_page.checking_value_of_basket_in_message()  # проверка стоимости корзины в сообщении

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.adding_an_product_to_basket()  # добавление товара в корзину
    product_page.solve_quiz_and_get_code()  # подсчет математического выражения в alert
    product_page.should_not_be_success_message()  # не должно быть сообщения об успехе


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()  # не должно быть сообщения об успехе

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.adding_an_product_to_basket()  # добавление товара в корзину
    product_page.solve_quiz_and_get_code()  # подсчет математического выражения в alert
    product_page.success_message_should_disappear()  # сообщение об успехе должно пропасть

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_no_product_in_basket()  # в корзине не должно быть товаров
    basket_page.presence_of_text_about_an_empty_basket()  # наличие текста о пустой корзине

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_login_page()

        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, '=-0987654')
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):  # пользователь не видит сообщение об успехе
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()  # не должно быть сообщения об успехе

    def test_user_can_add_product_to_basket(self, browser):  # пользователь может добавить товар в корзину
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.adding_an_product_to_basket()  # добавление товара в корзину
        product_page.solve_quiz_and_get_code()  # подсчет математического выражения в alert
        product_page.check_product_name_in_message()  # проверка название товара в сообщении
        product_page.checking_value_of_basket_in_message()  # проверка стоимости корзины в сообщении