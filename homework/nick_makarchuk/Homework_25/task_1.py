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


def test_submit_form(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    wait = WebDriverWait(driver, 10)
    text_input = wait.until(EC.presence_of_element_located((By.ID, 'id_text_string')))
    text_input.send_keys('Hello')
    text_input.send_keys(Keys.ENTER)
    result_text = wait.until(EC.visibility_of_element_located((By.ID, 'result-text'))).text
    print(result_text)
