require 'selenium-webdriver'
require 'webdrivers/chromedriver'
require_relative '../utils/file.rb'

module LoginWrongInputs
    def LoginWrongInputs.run
        driver = Selenium::WebDriver::Driver.for :chrome

        begin
            # driver.manage.window.maximize
            driver.navigate.to $domain
            
            $fluent_wait.until { driver.find_element(id: 'username').displayed? }
            inputUsername = driver.find_element(id: 'username')
            inputUsername.send_keys $wrong_username
            
            $fluent_wait.until { driver.find_element(id: 'password').displayed? }
            inputPassword = driver.find_element(id: 'password')
            inputPassword.send_keys $wrong_password
            
            $fluent_wait.until { driver.find_element(class: 'waves-button-input').displayed? }
            buttonSubmit = driver.find_element(class: 'waves-button-input')
            buttonSubmit.click

            $fluent_wait.until { driver.find_element(class: 'validation-summary-errors').displayed? }
        ensure
            driver.close
        end
    end
end
