from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


@pytest.fixture()
def driver():
    dr = webdriver.Chrome("chromedriver")
    dr.maximize_window()
    dr.get("https://dev.ole.bet/ru")
    return dr


@pytest.fixture()
def log_in(driver):
    wait = WebDriverWait(driver, 4)
    find_button_log = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[ng-reflect-translate="header.auth.login.title"]')))
    find_button_log.click()
    find_field_email = driver.find_element(By.ID, "loginFieldUsername").send_keys("storchak.eugene921@gmail.com")
    find_field_pass = driver.find_element(By.ID, "loginFieldPassword").send_keys("123456789q")
    find_button_login = driver.find_element(By.CLASS_NAME, "login__button-wrapper").click()
    time.sleep(3)
    icon_balance = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "profile__link")))
