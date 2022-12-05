import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from selenium.webdriver import ActionChains, Keys
import time
import pytest

from logs.logger import Logger


class Tools_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # locators
    drills = "//a[@href='/catalog/drills/']"
    rechargeable_drills = "//a[@href='/catalog/akkumulyatornye_dreli_shurupoverty/']"
    min_price = "//input[@class='min-price']"
    max_price = "//input[@class='max-price']"
    price_filter = "//div[@id='modef']"
    stomer_drill = "//*[@id='bx_1847241719_4456']/div/div/div/a"
    line_filter_for_stomer = "//a[@title='Отображать прайс-листом']"
    button_add_quantity = "/html/body/div[2]/div/div[2]/div/main/div[2]/div[2]/div/div/div/div/div[3]/div[1]/input"
    make_checkout = "//a[@class='btn']"
    checkout_button = "//button[@data-entity='basket-checkout-button']"

    # Getters

    def get_drills_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.drills)))

    def get_rechargeable_drills(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.rechargeable_drills)))

    def get_network_drills(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.network_drills)))

    def get_min_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.min_price)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_price)))


    def get_price_filter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_filter)))

    def get_stomer_drill(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.stomer_drill)))

    def get_line_filter_for_stomer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.line_filter_for_stomer)))

    def get_button_add_quantity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_quantity)))

    def get_drill_STOMER_SAD_98290103(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.drill_STOMER_SAD_98290103)))

    def get_make_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.make_checkout)))


    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))

    # Actions
    def click_get_drills_category(self):
        self.get_drills_category().click()
        self.get_current_url()
        print("Click Drills in catalog")

    def click_get_rechargeable_drills(self):
        self.get_rechargeable_drills().click()
        self.get_current_url()
        print("Click on Rechargeable Drills")

    def click_get_network_drills(self):
        self.get_network_drills().click()
        self.get_current_url()
        print("Click on Network Drills")

    """Фильтр товары от 1000р до 3000р"""
    def price_filter_3000(self):
        self.get_min_price().send_keys("1000")
        self.get_max_price().send_keys("3000")
        print("Used filter 1000-3000")
        self.get_max_price().send_keys(Keys.RETURN)


    # Methods
    """Найти Дрель STOMER SAD-10,8Nx2-LiD 98290103 и оформить покупку"""
    def click_drill_STOMER_SAD_98290103(self):
        with allure.step("Click drill STOMER SAD 98290103"):
            Logger.add_start_step(method="click_drill_STOMER_SAD_98290103")
            self.get_stomer_drill().click()
            print("used filter for Stomer drill")
            self.get_line_filter_for_stomer().click()
            print("used filter goods by a line")
            self.get_button_add_quantity().click()
            self.get_button_add_quantity().send_keys(Keys.TAB, Keys.TAB, Keys.ENTER)
            print("Product added to cart")
            self.get_make_checkout().click()
            self.get_checkout_button().click()
            Logger.add_end_step(url=self.driver.current_url, method="click_drill_STOMER_SAD_98290103")


