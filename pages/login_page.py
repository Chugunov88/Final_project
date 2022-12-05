import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from selenium.webdriver.chrome.options import Options

from logs.logger import Logger

opts = Options()

class Login_page(Base):



    url = 'https://murav.ru/personal/'
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver




    # Locators

    user_name = "//input[@name='USER_LOGIN']"
    password = "//input[@name='USER_PASSWORD']"
    login_button = "//button[@name='Login']"
    main_word = "//h1[@id='pagetitle']"

    # Getters


    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    # Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")


    def click_button(self):
        self.get_login_button().click()
        print("Click Login Button")


    # Methods

    def authorization(self):
        with allure.step("Authorization"):
            Logger.add_start_step(method="authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_user_name().click()
            self.input_user_name("9912447604")
            self.input_password("Quality902")
            self.click_button()
            self.assert_word(self.get_main_word(), "Персональный раздел")
            Logger.add_end_step(url=self.driver.current_url, method="authorization")