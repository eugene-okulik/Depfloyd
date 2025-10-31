from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    # sleep(3)
    chrome_driver.maximize_window()
    yield chrome_driver
    # sleep(3)
    chrome_driver.quit()


# def test_submit_form(driver):
#     driver.get('https://www.qa-practice.com/elements/input/simple')
#     wait = WebDriverWait(driver, 5)
#     text_input = driver.find_element(By.ID, 'id_text_string')
#     text_input.send_keys('Hello')
#     text_input.send_keys(Keys.ENTER)
#     result_text = wait.until(EC.visibility_of_element_located((By.ID, 'result-text'))).text
#     print(result_text)


def test_filling_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    first_name = driver.find_element(By.ID, 'firstName')
    first_name.send_keys('Nikolai')
    last_name = driver.find_element(By.ID, 'lastName')
    last_name.send_keys('Makarchuk')
    email = driver.find_element(By.ID, 'userEmail')
    email.send_keys('nikolai.makarchuk@example.com')
    gender_label = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
    gender_label.click()
    phone_number = driver.find_element(By.ID, 'userNumber')
    phone_number.send_keys('1234567890')
    date_of_birth = driver.find_element(By.ID, 'dateOfBirthInput')
    date_of_birth.send_keys('01/01/2000')
    subject = driver.find_element(By.ID, 'subjectsInput')
    subject.send_keys('Math')