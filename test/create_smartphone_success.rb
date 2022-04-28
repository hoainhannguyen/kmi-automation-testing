require 'selenium-webdriver'
require 'webdrivers/chromedriver'
# require_relative '../utils/file.rb'

module CreateSmartPhoneSuccess
    def CreateSmartPhoneSuccess.run
        driver = Selenium::WebDriver::Driver.for :chrome
        Selenium::WebDriver.logger.level = :warn
        Selenium::WebDriver.logger.output = FileUtils.get_file_path('../reports/logs.log')
        
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
            
            driver.navigate.to $devices_route

            sleep 1

            $fluent_wait.until { driver.find_element(css: 'button[aria-label="New Device"]').displayed? }
            buttonCreateDevice = driver.find_element(css: 'button[aria-label="New Device"]')
            buttonCreateDevice.click

            sleep 1

            $fluent_wait.until { driver.find_element(css: 'button.se-menuitem-createdevice[aria-label="Smartphone"]').displayed? }
            buttonCreatePhone = driver.find_element(css: 'button.se-menuitem-createdevice[aria-label="Smartphone"]')
            buttonCreatePhone.click

            sleep 1

            $fluent_wait.until { driver.find_element(css: "input[formControlName='deviceName']").displayed? }
            inputDeviceName = driver.find_element(css: "input[formControlName='deviceName']")
            inputDeviceName.send_keys $device_name

            sleep 1
            
            $fluent_wait.until { driver.find_element(css: "mat-select[formControlName='phoneAppInvite']").displayed? }
            selectAppName = driver.find_element(css: "mat-select[formControlName='phoneAppInvite']")
            selectAppName.click

            sleep 1
            
            $fluent_wait.until { driver.find_element(css: "mat-option").displayed? }
            selectAppName = driver.find_element(css: "mat-option")
            selectAppName.click

            sleep 1
            
            $fluent_wait.until { driver.find_element(css: ".btn-save-process button").displayed? }
            selectAppName = driver.find_element(css: ".btn-save-process button")
            selectAppName.click

            sleep 1
            
            $fluent_wait.until { driver.find_element(css: "kmi-quick-search input").displayed? }
            inputAccess = driver.find_element(css: "kmi-quick-search input")
            inputAccess.send_keys $device_access_name

            sleep 1
            
            $fluent_wait.until { driver.find_element(css: "mat-radio-button").displayed? }
            raidoButtonAccess = driver.find_element(css: "mat-radio-button")
            raidoButtonAccess.click

            sleep 1
            
            $fluent_wait.until { driver.find_element(css: ".btn-save-process .mat-flat-button").displayed? }
            buttonSaveDevice = driver.find_element(css: ".btn-save-process .mat-flat-button")
            buttonSaveDevice.click

            sleep 1

            $fluent_wait.until { driver.find_element(css: ".search-toolbar input").displayed? }
            inputAccess = driver.find_element(css: ".search-toolbar input")
            inputAccess.send_keys $device_name

            sleep 1

            $fluent_wait.until { driver.find_element(css: ".table-container--devicelist tbody tr").displayed? }
            tableRowDevice = driver.find_element(css: ".table-container--devicelist tbody tr")
            tableRowDevice.click

            sleep 1

            $fluent_wait.until { driver.find_element(css: ".se-device-detail-container").displayed? }
        rescue => exception
            puts exception
        ensure
            sleep 5
            driver.close
        end
    end
end
