import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import pytest

# не смог разобраться с прокси, временное решение
for var in ["HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"]:
    os.environ.pop(var, None)

# 4-05-32  video

@pytest.fixture
def driver():
    chrom_driver = webdriver.Chrome()
    chrom_driver.implicitly_wait(60)
    # sleep(4)
    chrom_driver.maximize_window()
    yield chrom_driver



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
    driver.get('https://uzum.uz/uz/product/erkaklar-uchun-ikki-1596531')
    size = driver.find_element(By.CLASS_NAME, 'active radio-image-wrapper').click()
    color = driver.find_element(By.TAG_NAME, '[alt="Koʻk"]').click()
    button = driver.find_element(By.TAG_NAME, '[data-test-id=button__add-cart]').click()
    counter = driver.find_element(By.CSS_SELECTOR, 'span.CaptionLRegular')
    # span.CaptionLRegular






