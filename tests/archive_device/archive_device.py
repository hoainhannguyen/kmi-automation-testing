import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


class ArchiveDeviceCase:
    def __init__(self, driver):
        self.driver = driver

    def run(self):
        try:
            assert isinstance(self.driver, webdriver.Chrome)
            wait = WebDriverWait(self.driver, timeout=10)
            configs = {}
            with open("configs/archive_device.json", encoding='utf-8') as jsonFile:
                configs = json.load(jsonFile)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[mattooltip='Quick Actions']")))
            self.driver.find_element(By.CSS_SELECTOR, "button[mattooltip='Quick Actions']").click()
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='More Options']")))
            self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='More Options']").click()
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Archive']")))
            self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Archive']").click()
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-save-process .mat-flat-button")))
            self.driver.find_element(By.CSS_SELECTOR, ".btn-save-process .mat-flat-button").click()
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-save-process .mat-flat-button")))
            self.driver.find_element(By.CSS_SELECTOR, ".btn-save-process .mat-flat-button").click()
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-save-process .mat-flat-button")))
            self.driver.find_element(By.CSS_SELECTOR, ".btn-save-process .mat-flat-button").click()
            sleep(1)

        except:
            print("ARCHIVE DEVICE ===========> FAILED")
        finally:
            for entry in self.driver.get_log("browser"):
                # print("ARCHIVE DEVICE ===========> PASSED")
                logger.log(entry)
