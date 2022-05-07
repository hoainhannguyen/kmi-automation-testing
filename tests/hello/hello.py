from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from utils.logger import logger


def run():
    service = Service("./webdrivers/chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    try:
        driver.get("https://www.python.org")
        sleep(1)
        search_bar = driver.find_element(by=By.NAME, value="q")
        search_bar.clear()
        sleep(1)
        search_bar.send_keys("getting started with python")
        sleep(1)
        search_bar.send_keys(Keys.RETURN)
    finally:
        for entry in driver.get_log("browser"):
            logger.log(entry)
        driver.quit()
