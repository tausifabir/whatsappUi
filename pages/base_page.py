from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_web_element(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_locator(by_locator))

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_locator(by_locator)).send_keys(text).click()

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_locator(by_locator))
        return bool(element)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)
