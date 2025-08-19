import os
from cmath import acosh
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# не смог разобраться с прокси, временное решение
for var in ["HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"]:
    os.environ.pop(var, None)

#   video

@pytest.fixture
def driver():
    chrom_driver = webdriver.Chrome()
    # sleep(4)
    chrom_driver.maximize_window()
    yield chrom_driver
    chrom_driver.quit()

def test_scroll(driver):
    driver.get('https://www.onliner.by/')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')


def test_scroll_to_element(driver):
    driver.get('https://the-internet.herokuapp.com/')
    sleep(3)
    link = driver.find_element(By.LINK_TEXT, 'JQuery UI Menus')
    driver.execute_script('arguments[0].scrollIntoView();', link)
    sleep(1)


def  test_upload(driver):
    driver.get('https://the-internet.herokuapp.com/upload')
    upload = driver.find_element(By.ID, 'file-upload')
    button = driver.find_element(By.ID, 'file-submit')
    upload.send_keys(r"C:\Users\mirzaali.abzalov\Desktop\Текстовый документ.txt")
    sleep(2)
    button.click()
    sleep(2)














