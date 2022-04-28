require 'selenium-webdriver'
require 'webdrivers/chromedriver'
require_relative '../utils/file.rb'

module LoginSuccess
    def LoginSuccess.run
        driver = Selenium::WebDriver::Driver.for :chrome
        Selenium::WebDriver.logger.level = :warn
        Selenium::WebDriver.logger.output = FileUtils.get_file_path('../logs/logs.log')

        begin
            driver.manage.window.maximize
            driver.navigate.to $domain

            sleep 1
            
            $fluent_wait.until { driver.find_element(id: 'username').displayed? }
            inputUsername = driver.find_element(id: 'username')
            inputUsername.send_keys $username

            sleep 1
            
            $fluent_wait.until { driver.find_element(id: 'password').displayed? }
            inputPassword = driver.find_element(id: 'password')
            inputPassword.send_keys $password

            sleep 1
            
            $fluent_wait.until { driver.find_element(class: 'waves-button-input').displayed? }
            buttonSubmit = driver.find_element(class: 'waves-button-input')
            buttonSubmit.click

            sleep 1
            
            $fluent_wait.until { driver.find_element(class: 'btn-message').displayed? }
            buttonAccept = driver.find_element(class: 'btn-message')
            buttonAccept.click

            sleep 1
            
            $fluent_wait.until { driver.find_element(class: 'toolbar-avatar').displayed? }
            avatarButton = driver.find_element(class: 'toolbar-avatar')
            avatarButton.click

            sleep 1

            $fluent_wait.until { driver.find_element(class: 'mat-list-item-avatar').displayed? }
            userDetailsButton = driver.find_element(class: 'mat-list-item-avatar')
            userDetailsButton.click

            sleep 1

            $fluent_wait.until { driver.find_element(class: 'se-user-detail-container').displayed? }
        rescue => exception
            puts exception
        ensure
            sleep 5
            driver.close
        end
    end
end
