require 'selenium-webdriver'
require 'webdrivers/chromedriver'

options = Selenium::WebDriver::Chrome::Options.new
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-translate')
driver = Selenium::WebDriver::Driver.for :chrome, options: options
wait = Selenium::WebDriver::Wait.new(timeout: 120, interval: 5, message: 'Timed out after 120 sec')

username = "haotran.081097@gmail.com"
password = "Haohao@1997"

driver.navigate.to "https://hana291020.360awareqa.com/"

wait.until { driver.find_element(id: "username").displayed? }
inputUsername = driver.find_element(id: "username")
inputUsername.send_keys username

wait.until { driver.find_element(id: "password").displayed? }
inputPassword = driver.find_element(id: "password")
inputPassword.send_keys password

wait.until { driver.find_element(class: "waves-button-input").displayed? }
buttonSubmit = driver.find_element(class: "waves-button-input")
buttonSubmit.click

wait.until { driver.find_element(class: "btn-message").displayed? }
buttonAccept = driver.find_element(class: "btn-message")
buttonAccept.click

wait.until { driver.find_element(class: "mat-toolbar").displayed? }

driver.close
