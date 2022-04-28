require 'selenium-webdriver'
require 'webdrivers/chromedriver'
require_relative '../utils/file.rb'

module LoginFailed
    def LoginFailed.run
        driver = Selenium::WebDriver::Driver.for :chrome
        Selenium::WebDriver.logger.level = :warn
        Selenium::WebDriver.logger.output = FileUtils.get_file_path('../reports/logs.log')

        begin
            driver.manage.window.maximize
            driver.navigate.to $domain

            sleep 1
            
            $fluent_wait.until { driver.find_element(id: 'username').displayed? }
            inputUsername = driver.find_element(id: 'username')
            inputUsername.send_keys $wrong_username

            sleep 1
            
            $fluent_wait.until { driver.find_element(id: 'password').displayed? }
            inputPassword = driver.find_element(id: 'password')
            inputPassword.send_keys $wrong_password

            sleep 1
            
            $fluent_wait.until { driver.find_element(class: 'waves-button-input').displayed? }
            buttonSubmit = driver.find_element(class: 'waves-button-input')
            buttonSubmit.click

            sleep 1

            $fluent_wait.until { driver.find_element(class: 'validation-summary-errors').displayed? }
        rescue => exception
            puts exception
        ensure
            driver.close
        end
    end
end
