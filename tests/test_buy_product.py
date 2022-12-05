import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


# from pages import personal_page
from pages.personal_page import Personal_page
from pages.tools import Tools_page
# from pages.client_information_page import Client_information_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from selenium.webdriver.chrome.options import Options

from utilities.conftest import set_up

# from pages.cart_page import Cart_page
# from pages.main_page import Main_page
# from pages.payment_page import Payment_page
# @pytest.mark.run(order=3)




"""Аккумуляторные дрели и шуруповёрты"""
def test_buy_products_1(set_up):
    options = Options()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    # options.add_argument("user-agent=[Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36]")
    driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\resource\\chromedriver.exe',
                              chrome_options=options)
    print("Start Test 1")

    """Открыть страницу логина и авторизоваться"""
    login = Login_page(driver)
    login.authorization()

    """Перейти на страницу электроинструмент"""
    sdc = Personal_page(driver)
    sdc.select_power_tool_page()

    """Кликнуть аккумуляторные дрелли и шуруповёрты"""
    cdc = Tools_page(driver)
    cdc.click_get_rechargeable_drills()

    """Задать фильтра"""
    cdc.price_filter_3000()

    """Выбрать дрель STOMER_SAD_98290103"""
    cdc.click_drill_STOMER_SAD_98290103()

    """Финальная страница заказа, сравнить url и сделать скриншот"""

    f = Finish_page(driver)
    f.finish()
    # time.sleep(10)
    time.sleep(15)
    driver.quit()

