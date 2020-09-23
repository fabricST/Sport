import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_make_bet(driver, log_in):
    wait = WebDriverWait(driver, 30)
    find_prematch_tab = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[ng-reflect-translate="menu.sport"]')))
    find_prematch_tab.click()
    time.sleep(5)
    find_sport_page = wait.until(EC.visibility_of_element_located((By.ID, "app")))

