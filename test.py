import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from oxwall_test_project.oxwall_home_work.custom_waits import presence_of_elements
from oxwall_test_project.oxwall_home_work.oxwall_helper import OxwallHelper
from selenium.webdriver.support.ui import Select


# def test_registration(driver):

base_url = 'http://localhost:8888/oxwall/'

dr = webdriver.Chrome(executable_path=r"/Users/fabric/PycharmProjects/chromedriver")
dr.maximize_window()
dr.get(base_url)
wait = WebDriverWait(dr, 4)

sing_up = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ow_console_item_link')))
sing_up.click()
field_user_name = wait.until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'ow_username_validator')))
field_user_name[0].send_keys('Alex')
field_email = dr.find_element(By.NAME, "email").send_keys('storchak.eugene2@gmail.com')
field_password = wait.until(EC.visibility_of_any_elements_located((By.NAME, 'password')))
field_password[0].send_keys('pass')
field_repeat_password = dr.find_element(By.NAME, 'repeatPassword').send_keys('pass')
field_real_name = wait.until(
    EC.visibility_of_any_elements_located((By.XPATH, '//label[text()="Real name"]/../..//input')))
field_real_name[0].send_keys("No name")

field_checkbox_gender = wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//label[text()="Male"]/.')))
field_checkbox_gender[0].click()

select_birthday_field = wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//label[contains(text(), "Birthday")]/../../td[2]/div/div[1]/select')))
select_birthday = Select(select_birthday_field[0])
select_birthday.select_by_value('2')
select_month_field = wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//label[contains(text(), "Birthday")]/../../td[2]/div/div[2]/select')))
select_month = Select(select_month_field[0])
select_month.select_by_value('8')
select_year_field = wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//label[contains(text(), "Birthday")]/../../td[2]/div/div[3]/select')))
select_year = Select(select_year_field[0])
select_year.select_by_value('1980')

find_checkbox_look = wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//label[contains(text(), "Looking for")]')))
find_checkbox_look[0].click()

