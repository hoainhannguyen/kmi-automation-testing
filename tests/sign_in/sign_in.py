import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger
from utils.settings import global_settings


def run():
    service = Service("webdrivers/chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    try:
        wait = WebDriverWait(driver, timeout=10)
        configs = {}
        with open("configs/sign_in.json", encoding='utf-8') as jsonFile:
            configs = json.load(jsonFile)
        driver.get(configs["default"]["domain"])
        wait.until(EC.visibility_of_element_located((By.ID, "username")))
        driver.find_element(by=By.ID, value="username").send_keys(configs["default"]["username"])
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.ID, "password")))
        driver.find_element(by=By.ID, value="password").send_keys(configs["default"]["password"])
        sleep(1)
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "waves-button-input")))
        driver.find_element(by=By.CLASS_NAME, value="waves-button-input").click()
        sleep(5)
    finally:
        for entry in driver.get_log("browser"):
            logger.log(entry)
        driver.quit()
