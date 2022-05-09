import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import logger


class NewDeviceCase:
    def __init__(self, driver):
        self.driver = driver

    def run(self):
        try:
            assert isinstance(self.driver, webdriver.Chrome)
            wait = WebDriverWait(self.driver, timeout=10)
            configs = {}
            with open("configs/new_device.json", encoding='utf-8') as jsonFile:
                configs = json.load(jsonFile)
            wait.until(EC.visibility_of_element_located((By.NAME, "button")))
            self.driver.find_element(By.NAME, "button").click()
            sleep(1)
            self.driver.get(configs["default"]["devicesURL"])
            sleep(1)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label='New Device']")))
            self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='New Device']").click()
            sleep(1)
            wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "button.se-menuitem-createdevice[aria-label='Smartphone']")))
            self.driver.find_element(By.CSS_SELECTOR,
                                     "button.se-menuitem-createdevice[aria-label='Smartphone']").click()
            sleep(1)
            wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[formControlName='deviceName']")))
            self.driver.find_element(
                By.CSS_SELECTOR, "input[formControlName='deviceName']").send_keys(
                configs["default"]["deviceName"])
            sleep(1)
            wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "mat-select[formControlName='phoneAppInvite']")))
            self.driver.find_element(By.CSS_SELECTOR, "mat-select[formControlName='phoneAppInvite']").click()
            sleep(1)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "mat-option")))
            self.driver.find_element(By.CSS_SELECTOR, "mat-option").click()
            sleep(1)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-save-process button")))
            self.driver.find_element(By.CSS_SELECTOR, ".btn-save-process button").click()
            sleep(1)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "kmi-quick-search input")))
            self.driver.find_element(
                By.CSS_SELECTOR, "kmi-quick-search input").send_keys(configs["default"]["accessName"])
            sleep(1)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "mat-radio-button")))
            self.driver.find_element(By.CSS_SELECTOR, "mat-radio-button").click()
            sleep(1)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-save-process .mat-flat-button")))
            self.driver.find_element(By.CSS_SELECTOR, ".btn-save-process .mat-flat-button").click()
            sleep(1)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-toolbar input")))
            self.driver.find_element(
                By.CSS_SELECTOR, ".search-toolbar input").send_keys(configs["default"]["deviceName"])
            sleep(1)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".table-container--devicelist tbody tr")))
            self.driver.find_element(By.CSS_SELECTOR, ".table-container--devicelist tbody tr").click()
            sleep(1)
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".se-device-detail-container")))
            sleep(1)
        except:
            print("NEW DEVICE ===========> FAILED")
        finally:
            for entry in self.driver.get_log("browser"):
                logger.log(entry)
