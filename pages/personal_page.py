import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from logs.logger import Logger


class Personal_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    catalog = "//a[@class='head']"
    power_tool = "/html/body/div[2]/header/div[4]/div/nav/div/ul/li[2]/a/span"
    power_tool_word = "//h1[@id='pagetitle']"



    # Getters

    def get_power_tool_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.power_tool_word)))


    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))


    def get_power_tool(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.power_tool)))




    # Actions

    def click_get_catalog(self):
        self.get_catalog().click()
        print("Click catalog")

    def click_get_power_tool(self):
        self.get_power_tool().click()
        print("Click power tool")


    # Methods

    def select_power_tool_page(self):
        with allure.step("Select power tool page"):
            Logger.add_start_step(method="select_power_tool_page")
            self.get_current_url()
            self.driver.maximize_window()
            self.click_get_catalog()
            self.click_get_power_tool()
            self.assert_url("https://murav.ru/catalog/tools/")
            Logger.add_end_step(url=self.driver.current_url, method="select_power_tool_page")







