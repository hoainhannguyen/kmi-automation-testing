require 'selenium-webdriver'

no_such_element_error = Selenium::WebDriver::Error::NoSuchElementError

$explicit_wait = Selenium::WebDriver::Wait.new(timeout: 30, interval: 5, message: 'Timed out after 30 sec')

$fluent_wait = Selenium::WebDriver::Wait.new(timeout: 30, interval: 5, message: 'Timed out after 30 sec', ignore: no_such_element_error)
