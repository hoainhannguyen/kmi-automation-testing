# MODULES
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Utils
from ..utils import logger

def run():
    # Chrome Driver Configs
    service = Service("./webdrivers/chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    # Set up Chrome Driver
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    # Begin
    sleep(1)
    driver.get("https://www.python.org")
    sleep(1)
    search_bar = driver.find_element(by=By.NAME, value="q")
    search_bar.clear()
    sleep(1)
    search_bar.send_keys("getting started with python")
    sleep(1)
    search_bar.send_keys(Keys.RETURN)
    sleep(1)
    driver.implicitly_wait(30)
    # LOGGING
    for entry in driver.get_log("browser"):
        logger.log(entry)
    # Close Driver
    driver.close()
    # End
