from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep


@pytest.fixture()
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.maximize_window()
    chrome_driver.implicitly_wait(2)
    yield chrome_driver
    chrome_driver.quit()


def test_tab(driver):
    driver.get('http://testshop.qa-practice.com/')
    wait = WebDriverWait(driver, 5)
    item = driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/customizable-desk-9"]')
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.click(item)
    actions.key_up(Keys.CONTROL)
    actions.perform()
    sleep(3)
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_cart = driver.find_element(By.ID, 'add_to_cart')
    add_to_cart.click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn-secondary')))
    button_continue = driver.find_element(By.CSS_SELECTOR, 'button.btn-secondary')
    button_continue.click()
    sleep(3)
