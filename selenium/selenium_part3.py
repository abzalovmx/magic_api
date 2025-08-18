import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# не смог разобраться с прокси, временное решение
for var in ["HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"]:
    os.environ.pop(var, None)

# 4-05-32  video

@pytest.fixture
def driver():
    chrom_driver = webdriver.Chrome()
    chrom_driver.implicitly_wait(10)
    # sleep(4)
    chrom_driver.maximize_window()
    yield chrom_driver
    chrom_driver.quit()



def test_clear(driver):
    input_data = "enter"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    txt_string = driver.find_element(By.NAME, "text_string")
    txt_string.send_keys(input_data)
    sleep(2)
    # txt_string.clear()
    entered_data = txt_string.get_attribute("value")
    for _ in range(len(entered_data)):
        txt_string.send_keys(Keys.BACKSPACE)
    assert txt_string.is_displayed()


def test_enabled_and_select(driver):
    driver.get('https://www.qa-practice.com/elements/button/disabled')
    button = driver.find_element(By.NAME, "submit")
    print(button.is_enabled())
    selector = driver.find_element(By.ID, 'id_select_state')
    dropdown = Select(selector)
    dropdown.select_by_value('enabled')
    print(button.is_enabled())


def test_welcome(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    driver.find_element(By.CSS_SELECTOR, '#start button').click()
    assert driver.find_element(By.ID, 'finish').text == 'Hello World!'


def test_cart(driver):
    driver.get('https://magento.softwaretestingboard.com/argus-all-weather-tank.html')
    driver.find_element(By.ID, 'option-label-size-143-item-166').click()
    driver.find_element(By.ID, 'option-label-color-93-item-52').click()
    button = driver.find_element(By.ID, 'product-addtocart-button')
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    button.click()
    wait = WebDriverWait(driver, 5)
    wait.until_not(EC.text_to_be_present_in_element_attribute(
        (By.CSS_SELECTOR, '.counter.qty'),
        'class',
        'empty'
    ))
    wait.until_not(EC.text_to_be_present_in_element_attribute(
        (By.CSS_SELECTOR, '.counter.qty'),
        'class',
        'loading'
    ))
    counter = driver.find_element(By.CSS_SELECTOR, '.counter-number')
    print(counter.text)


def test_5_sec2(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.ID, 'visibleAfter')))
    button3 = driver.find_element(By.ID, 'visibleAfter')
    button3.click()
    print(driver.get_cookies())
    # driver.add_cookie({'name': 'name'})


def test_same_el(driver):
    driver.get('https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html')
    product_link = driver.find_elements(By.CLASS_NAME, 'product-item-link')
    print(product_link[0].text)


def test_same_els(driver):
    driver.get('https://magento.softwaretestingboard.com/men/bottoms-men/pants-men.html')
    product_link = driver.find_elements(By.CLASS_NAME, 'product-item-info')
    print(product_link[0].find_element(By.CLASS_NAME, 'price'))