from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.maximize_window()
    yield chrome_driver
    chrome_driver.quit()


def test_tab(driver):
    driver.get('http://testshop.qa-practice.com/')
    item = driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/customizable-desk-9"]')
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.click(item)
    actions.key_up(Keys.CONTROL)
    actions.perform()