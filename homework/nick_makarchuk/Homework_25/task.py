from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = 'eager'
    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(2)
    yield chrome_driver
    chrome_driver.quit()


def test_submit_form(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    wait = WebDriverWait(driver, 5)
    text_input = driver.find_element(By.ID, 'id_text_string')
    text_input.send_keys('Hello_first_task')
    text_input.send_keys(Keys.ENTER)
    result_text = wait.until(EC.visibility_of_element_located((By.ID, 'result-text'))).text
    print(result_text)


def test_filling_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    wait = WebDriverWait(driver, 5)
    wait.until(EC.presence_of_element_located((By.ID, 'firstName')))
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
    date_of_birth.click()
    date_of_birth.send_keys(Keys.CONTROL + 'a')
    date_of_birth.send_keys('01 Jan 2000')
    date_of_birth.send_keys(Keys.ENTER)
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '.modal.show')))
    subject = driver.find_element(By.ID, 'subjectsInput')
    subject.send_keys('Math')
    subject.send_keys(Keys.ENTER)
    checkbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]')))
    driver.execute_script("arguments[0].click();", checkbox)
    adress = driver.find_element(By.ID, 'currentAddress')
    adress.send_keys('125368, Russia, Moscow, Mitinskaya street, 10')
    state_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#state')))
    driver.execute_script("arguments[0].scrollIntoView(true);", state_container)
    driver.execute_script("arguments[0].click();", state_container)
    state_input = wait.until(EC.presence_of_element_located((By.ID, 'react-select-3-input')))
    state_input.send_keys('NCR')
    state_input.send_keys(Keys.ENTER)
    city_container = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#city')))
    driver.execute_script("arguments[0].scrollIntoView(true);", city_container)
    driver.execute_script("arguments[0].click();", city_container)
    city_input = wait.until(EC.element_to_be_clickable((By.ID, 'react-select-4-input')))
    city_input.send_keys('Delhi')
    city_input.send_keys(Keys.ENTER)
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, 'submit')))
    submit_button.click()
    result_table = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.table-responsive')))
    result_text_form = result_table.text
    print(result_text_form)


def test_submit_with_assert(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    form_select = driver.find_element(By.ID, 'id_choose_language')
    form_select.click()
    select_option = driver.find_element(By.XPATH, "//option[text()='Python']")
    select_option.click()
    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()
    result_text = driver.find_element(By.ID, 'result-text')
    assert result_text.text == 'Python'
    print(result_text.text)


def test_dynamic_loading(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.CSS_SELECTOR, 'div.example button')
    start_button.click()
    driver.implicitly_wait(10)
    hello_world_text = driver.find_element(By.ID, 'finish')
    assert hello_world_text.text == 'Hello World!'
    print(hello_world_text.text)
