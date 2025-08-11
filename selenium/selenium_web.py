import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# не смог разобраться с прокси, временное решение
for var in ["HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"]:
    os.environ.pop(var, None)

options = Options()
options.add_argument("start-maximized")


driver = webdriver.Chrome(options=options)
sleep(3)
driver.maximize_window()
# driver.set_window_size(1920, 1080)
driver.get("https://google.com")

# 45-48




sleep(3)