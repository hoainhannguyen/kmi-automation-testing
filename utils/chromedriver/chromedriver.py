from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("webdrivers/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


class ChromeDriver:
    def __init__(self):
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(30)

    def maximize(self):
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()
