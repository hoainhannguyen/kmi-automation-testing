import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


class DeleteDeviceCase:
    def __init__(self, driver):
        self.driver = driver

    def run(self):
        status = True
        try:
            assert isinstance(self.driver, webdriver.Chrome)
            wait = WebDriverWait(self.driver, timeout=10)
            configs = {}
            with open("configs/delete_device.json", encoding='utf-8') as jsonFile:
                configs = json.load(jsonFile)

            self.driver.get(configs["default"]["devicesURL"])
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-toolbar input")))
            self.driver.find_element(By.CSS_SELECTOR, ".search-toolbar input").send_keys(configs["devicesURL"]["deviceName"])
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[mattooltip='Quick Actions']")))
            self.driver.find_element(By.CSS_SELECTOR, "button[mattooltip='Quick Actions']").click()
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='More Options']")))
            self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='More Options']").click()
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button mat-icon[svgicon='ic_delete_48px']")))
            self.driver.find_element(By.CSS_SELECTOR, "button mat-icon[svgicon='ic_delete_48px']").click()
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-save-process .mat-flat-button")))
            self.driver.find_element(By.CSS_SELECTOR, ".btn-save-process .mat-flat-button").click()
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[mattooltip='Quick Actions']")))
            self.driver.find_element(By.CSS_SELECTOR, "button[mattooltip='Quick Actions']").click()
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='More Options']")))
            self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='More Options']").click()
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button mat-icon[svgicon='ic_delete_forever_24px']")))
            self.driver.find_element(By.CSS_SELECTOR, "button mat-icon[svgicon='ic_delete_forever_24px']").click()
            sleep(2)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[placeholder='Type Delete']")))
            self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='Type Delete']").send_keys(configs["devicesURL"]["confirmText"])
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-save-process .mat-flat-button")))
            self.driver.find_element(By.CSS_SELECTOR, ".btn-save-process .mat-flat-button").click()
            sleep(1)

        except:
            status = False
        finally:
            for entry in self.driver.get_log("browser"):
                logger.log(entry)
            return status
