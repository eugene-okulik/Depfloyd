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
    chrome_driver.implicitly_wait(2)
    yield chrome_driver
    chrome_driver.quit()


def test_tab(driver):
    driver.get('http://testshop.qa-practice.com/')
    wait = WebDriverWait(driver, 10)
    item = driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/customizable-desk-9"]')
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.click(item)
    actions.key_up(Keys.CONTROL)
    actions.perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    add_to_cart = driver.find_element(By.ID, 'add_to_cart')
    add_to_cart.click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn-secondary')))
    button_continue = driver.find_element(By.CSS_SELECTOR, 'button.btn-secondary')
    button_continue.click()
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div.modal.show')))
    driver.close()
    driver.switch_to.window(tabs[0])
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/shop/cart"]')))
    cart = driver.find_element(By.CSS_SELECTOR, 'a[href="/shop/cart"]')
    cart.click()
    wait.until(EC.url_contains('/shop/cart'))
    wait.until(EC.presence_of_element_located((By.XPATH, "//h6[contains(text(), 'Customizable Desk')]")))
    order_item = driver.find_element(By.XPATH, "//h6[contains(text(), 'Customizable Desk')]")
    assert order_item.text == 'Customizable Desk (Steel, White)'
    print(order_item.text)


def test_popup(driver):
    driver.get('http://testshop.qa-practice.com/')
    actions = ActionChains(driver)
    busket_button = driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-primary.a-submit')
    actions.move_to_element(busket_button)
    actions.click(busket_button)
    actions.perform()
    item = driver.find_element(By.CSS_SELECTOR, 'strong.product-name.product_display_name')
    assert item.text == '[FURN_0096] Customizable Desk (Steel, White)'
    print(item.text)
