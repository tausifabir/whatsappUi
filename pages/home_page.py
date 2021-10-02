import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementExpection
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import expected_conditions as EC


class HomePage(BasePage):
    SearchBox = (By.XPATH, "/html/body/div[1]/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]")

    # constructor of the page class
    def __init__(self, driver):
        super().__init__(driver)
