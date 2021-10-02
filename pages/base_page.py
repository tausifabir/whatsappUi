from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_web_element(self, by_locator):
        WebDriverWait(self.driver, 10).until(Ec.visibility_of_element_locator(by_locator))

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(Ec.visibility_of_element_locator(by_locator)).send_keys(text).click()

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(Ec.visibility_of_element_located(by_locator)).click()
