import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# не смог разобраться с прокси, временное решение
for var in ["HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"]:
    os.environ.pop(var, None)

options = Options()
options.add_argument("start-maximized")


driver = webdriver.Chrome(options=options)
sleep(2)
driver.maximize_window()
# driver.set_window_size(1920, 1080)
# options.add_experimental_option("detach", True)
driver.get("https://google.com")
print(driver.title)
print(driver.current_url)
# 1-19-27




sleep(3)