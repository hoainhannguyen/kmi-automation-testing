require 'selenium-webdriver'

webDriver_error = Selenium::WebDriver::Error::WebDriverError
timeout_error = Selenium::WebDriver::Error::TimeoutError
no_such_element_error = Selenium::WebDriver::Error::NoSuchElementError

$explicit_wait = Selenium::WebDriver::Wait.new(timeout: 30, interval: 5, message: 'Timed out after 30 sec')

$fluent_wait = Selenium::WebDriver::Wait.new(timeout: 30, interval: 5, message: 'Timed out after 30 sec', ignore:webDriver_error)
