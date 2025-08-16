import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

# не смог разобраться с прокси, временное решение
for var in ["HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"]:
    os.environ.pop(var, None)

# 3-13-41  video

@pytest.fixture
def driver():
    chrom_driver = webdriver.Chrome()
    chrom_driver.maximize_window()
    yield chrom_driver
    sleep(2)

def test_input(driver):
    input_data = "enter"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    txt_string = driver.find_element(By.CLASS_NAME, "textinput")
    txt_string.send_keys(input_data)
    txt_string.send_keys(Keys.ENTER)
    res = driver.find_element(By.ID, 'result-text')
    assert res.text == input_data

def test_classname(driver):
    input_data = "enter"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    # txt_string = driver.find_element(By.ID, "id_text_string")
    txt_string = driver.find_element(By.NAME, "text_string")
    txt_string.send_keys(input_data)
    # txt_string.submit()
    txt_string.send_keys(Keys.ENTER)
    res = driver.find_element(By.CLASS_NAME, 'result-text')
    assert res.text == input_data

def test_tag_name(driver):
    input_data = "Input field"
    driver.get("https://www.qa-practice.com/elements/input/simple")
    assert driver.find_element(By.TAG_NAME, "h1").text == input_data

def test_link(driver):
    driver.get("https://www.qa-practice.com/elements/input/simple")
    contact = driver.find_element(By.LINK_TEXT, "Contact")
    contact.click()
    assert driver.find_element(By.TAG_NAME, "h1").text == "Contact us"


def test_css_selector(driver):
    driver.get("https://www.qa-practice.com/elements/input/simple")
    txt_str = driver.find_element(By.CSS_SELECTOR, '[placeholder="Submit me"]')
    txt_str.send_keys("Submit")
    # txt_str.send_keys(Keys.ENTER)
    print(txt_str.value_of_css_property('border-color'))
    print(txt_str.get_attribute('innerText'))
    print(txt_str.text)
    assert txt_str.get_attribute("value") == "Submit"


def test_xpath(driver):
    driver.get("https://www.qa-practice.com/elements/input/simple")
    txt_str = driver.find_element(By.XPATH, '//input[@placeholder="Submit me"]')
    txt_str.send_keys("Submit")



















