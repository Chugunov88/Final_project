import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from logs.logger import Logger


class Finish_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators



    # Getters



    # Actions



    # Methods

    def finish(self):
        with allure.step("Finish"):
            Logger.add_start_step(method="finish")
            self.get_current_url()
            self.assert_url("https://murav.ru/personal/order/make/")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="finish")

