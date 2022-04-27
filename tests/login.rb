require 'selenium-webdriver'
require 'webdrivers/chromedriver'
require_relative '../utils/wait.rb'

module Login
    def Login.run
        driver = Selenium::WebDriver::Driver.for :chrome
        
        username = 'haotran.081097@gmail.com'
        password = 'Haohao@1997'
        
        begin
            driver.manage.window.maximize
            driver.navigate.to 'https://hana291020.360awareqa.com/'
            
            $fluent_wait.until { driver.find_element(id: 'username').displayed? }
            inputUsername = driver.find_element(id: 'username')
            inputUsername.send_keys username
            
            $fluent_wait.until { driver.find_element(id: 'password').displayed? }
            inputPassword = driver.find_element(id: 'password')
            inputPassword.send_keys password
            
            $fluent_wait.until { driver.find_element(class: 'waves-button-input').displayed? }
            buttonSubmit = driver.find_element(class: 'waves-button-input')
            buttonSubmit.click
            
            $fluent_wait.until { driver.find_element(class: 'btn-message').displayed? }
            buttonAccept = driver.find_element(class: 'btn-message')
            buttonAccept.click
            
            $fluent_wait.until { driver.find_element(class: 'mat-toolbar').displayed? }
        ensure
            driver.close
        end
    end
end
