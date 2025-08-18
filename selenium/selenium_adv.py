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

def test_new_tab(driver):
    driver.get("https://www.qa-practice.com/elements/new_tab/link")
    driver.find_element(By.ID, "new-page-link").click()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    result = driver.find_element(By.ID, "result-text")
    assert result.text == "I am a new page in a new tab"
    driver.close()
    driver.switch_to.window(tabs[0])


def test_iframe(driver):
    driver.get("https://www.qa-practice.com/elements/iframe/iframe_page")
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)
    burger_menu = driver.find_element(By.CLASS_NAME, "navbar-toggler-icon")
    burger_menu.click()
    sleep(2)
    driver.switch_to.default_content()
    driver.find_element(By.LINK_TEXT, "Iframe").click()


def test_stale_expection(driver):
    driver.get("https://www.qa-practice.com/elements/checkbox/single_checkbox")
    checkbox = driver.find_element(By.ID, "id_checkbox_0")
    checkbox.click()
    submit = driver.find_element(By.ID, "submit-id-submit")
    submit.click()
    assert driver.find_element(By.ID, "result-text").text == "select me or not"
    checkbox.click()
    submit.click()


def test_drop_menu(driver):
    driver.get("https://www.classmarker.com/")
    tour = driver.find_element(By.ID, "takeatour")
    works = driver.find_element(By.XPATH, '//*[@id="mainMenu"]/div/nav/ul/li[2]/div/ul/li[1]/a')
    # ActionChains(driver).move_to_element(tour).move_to_element(works).click(works).perform()
    actions = ActionChains(driver)
    actions.move_to_element(tour)
    actions.move_to_element(works)
    actions.click(works)
    actions.perform()


def test_drag_drop(driver):
    driver.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    first = driver.find_element(By.ID, 'rect-draggable')
    second = driver.find_element(By.ID, 'rect-droppable')
    # ActionChains(driver).drag_and_drop(first, second).perform()
    actions = ActionChains(driver)
    actions.click_and_hold(first)
    actions.move_to_element(second)
    actions.release()
    actions.perform()


def test_open_in_new_tab(driver):
    driver.get("https://www.qa-practice.com/elements/new_tab/link")
    link = driver.find_element(By.LINK_TEXT, "Homepage")
    ActionChains(driver).key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()
    sleep(1)


def test_alerts(driver):
    driver.get("https://www.qa-practice.com/elements/alert/alert")
    driver.find_element(By.CLASS_NAME, "a-button").click()
    alert = Alert(driver)
    alert.accept()
    sleep(1)