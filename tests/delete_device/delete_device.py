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
        try:
            assert isinstance(self.driver, webdriver.Chrome)
            wait = WebDriverWait(self.driver, timeout=10)
            configs = {}
            with open("configs/delete_device.json", encoding='utf-8') as jsonFile:
                configs = json.load(jsonFile)

            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='mat-checkbox-34']/label")))
            self.driver.find_element(By.XPATH, "//*[@id='mat-checkbox-34']/label").click()
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='More Actions']")))
            self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='More Actions']").click()
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Delete']")))
            self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Delete']").click()
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.ID, "mat-input-5")))
            self.driver.find_element(By.ID, "mat-input-5").send_keys(configs["default"]["typeDelete"])
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-save-process .mat-flat-button")))
            self.driver.find_element(By.CSS_SELECTOR, ".btn-save-process .mat-flat-button").click()
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='mat-checkbox-34']/label")))
            self.driver.find_element(By.XPATH, "//*[@id='mat-checkbox-34']/label").click()
            sleep(2)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='More Actions']")))
            self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='More Actions']").click()
            sleep(2)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='Permanently Delete']")))
            self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='Permanently Delete']").click()
            sleep(2)

            wait.until(EC.visibility_of_element_located((By.ID, "mat-input-7")))
            self.driver.find_element(By.ID, "mat-input-7").send_keys(configs["default"]["typeDelete"])
            sleep(1)

            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-save-process .mat-flat-button")))
            self.driver.find_element(By.CSS_SELECTOR, ".btn-save-process .mat-flat-button").click()
            sleep(1)

        except:
            print("DELETE DEVICE ===========> FAILED")
        finally:
            for entry in self.driver.get_log("browser"):
                # print("DELETE DEVICE ===========> PASSED")
                logger.log(entry)
