import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sport_helper


def test_registr(driver):
    wait = WebDriverWait(driver, 4)

    button_registration = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                       '.btn-bordered.registration-button.button-colored')))
    button_registration.click()

# Окно первое
    email = sport_helper.random_email()
    email_field = driver.find_element(By.ID, "registrationFormEmail").send_keys(email)
    pass_field = driver.find_element(By.ID, 'RegistrationFormPassword').send_keys('123456789q')
    button_next = driver.find_element(By.CSS_SELECTOR, '.button-colored.ladda-button').click()


# Окно второе
    name = sport_helper.random_name(5)
    surname = sport_helper.random_surname(7)
    wait = WebDriverWait(driver, 4)
    element2 = wait.until(EC.visibility_of_element_located((By.ID, 'registrationFormFirstName')))
    element2.send_keys(name)
    surname_field = driver.find_element(By.ID, 'registrationFormLastName').send_keys(surname)
    date_field = driver.find_element(By.ID, 'birthdayDay').send_keys('10')
    month_field = driver.find_element(By.ID, 'birthdayMM').send_keys('09')
    year_field = driver.find_element(By.ID, 'birthdayYY').send_keys('1982')
    button_next2 = driver.find_elements(By.CSS_SELECTOR, '.button-colored.ladda-button')[1]
    button_next2.click()


#  Окно третье
    phone = sport_helper.random_phone()
    country_field = driver.find_elements(By.CSS_SELECTOR, '.ng-input')[1]
    country_field.click()
    select_country = driver.find_elements(By.CSS_SELECTOR, '.ng-option-label')[5]
    select_country.click()
    fill_country = driver.find_element(By.ID, 'registrationFormCity').send_keys('First Tewst')
    fill_address = driver.find_element(By.ID, 'registrationFormAddress').send_keys('test reeltest')
    fill_phone = driver.find_element(By.ID, 'registrationFormPhoneNumber').send_keys(phone)
    fill_zip = driver.find_element(By.ID, 'registrationFormZipCode').send_keys('87363')
    button_next3 = driver.find_elements(By.CSS_SELECTOR, '.button-colored.ladda-button')[2]
    button_next3.click()


#  Окно четвертое
    wait = WebDriverWait(driver, 4)
    open_currency_field = wait.until(EC.visibility_of_element_located((By.XPATH, "//form[4]/div[1]/div[1]/div[1]/div/"
                                                                                 "ng-select/div/div")))
    open_currency_field.click()
    select_currency_eur = driver.find_element(By.XPATH, "//div/ng-select/ng-dropdown-panel/div/div[2]/div[1]/span")
    select_currency_eur.click()

    find_promocod_field = driver.find_element(By.ID, "registrationPromoCode").send_keys("2032")

    select_checkbox_terms = driver.find_elements(By.CSS_SELECTOR, '[ng-reflect-translate="registration.acceptRules"]')
    select_checkbox_terms[0].click()

    select_checkbox_policy = driver.find_elements(By.CSS_SELECTOR, '[ng-reflect-translate="registration.acceptRules"]')
    select_checkbox_policy[1].click()

    find_register_button = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-registration-modal/div[2]/"
                                                     "app-registration-4-steps/div/form[4]/div[2]/div[1]/button")
    find_register_button.click()

    time.sleep(2)
    after_registration_windows = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/"
                                                           "registration-verify-email/div[2]/div/div[2]/button")
    after_registration_windows.click()


# вход на почтовый ящик и подтверждение регистрации
    a = sport_helper.click_on_email()
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(a)
    time.sleep(3)
