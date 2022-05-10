import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


class SignInCase:
    def __init__(self, driver):
        self.driver = driver

    def run(self):
        status = True
        try:
            assert isinstance(self.driver, webdriver.Chrome)
            wait = WebDriverWait(self.driver, timeout=10)
            configs = {}
            globalSettings = {}
            with open("configs/sign_in.json", encoding='utf-8') as signInFile:
                configs = json.load(signInFile)
            with open("configs/global_settings.json", encoding='utf-8') as globalSettingsFile:
                globalSettings = json.load(globalSettingsFile)

            self.driver.get(globalSettings["domain"])
            sleep(10)

            wait.until(EC.visibility_of_element_located((By.ID, "username")))
            self.driver.find_element(By.ID, "username").send_keys(configs["default"]["username"])
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.ID, "password")))
            self.driver.find_element(By.ID, "password").send_keys(configs["default"]["password"])
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "waves-button-input")))
            self.driver.find_element(By.CLASS_NAME, "waves-button-input").click()
            sleep(1)

            if configs["default"]["eula"] == 1:
                wait.until(EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".btn-message .btn-submit.waves-effect.btn-flat")))
                self.driver.find_element(By.CSS_SELECTOR, ".btn-message .btn-submit.waves-effect.btn-flat").click()
                sleep(10)

            sleep(5)
        except:
            status = False
        finally:
            for entry in self.driver.get_log("browser"):
                logger.log(entry)
            return status
