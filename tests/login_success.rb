require 'selenium-webdriver'
require 'webdrivers/chromedriver'
require_relative '../utils/file.rb'

module LoginSuccess
    def LoginSuccess.run
        driver = Selenium::WebDriver::Driver.for :chrome

        reoprtFilePath = FileUtils.get_file_path('../reports/index.html')
        reoprtFile = File.new(reoprtFilePath, 'r+')

        begin
            # driver.manage.window.maximize
            driver.navigate.to $domain
            
            $fluent_wait.until { driver.find_element(id: 'username').displayed? }
            inputUsername = driver.find_element(id: 'username')
            inputUsername.send_keys $username
            
            $fluent_wait.until { driver.find_element(id: 'password').displayed? }
            inputPassword = driver.find_element(id: 'password')
            inputPassword.send_keys $password
            
            $fluent_wait.until { driver.find_element(class: 'waves-button-input').displayed? }
            buttonSubmit = driver.find_element(class: 'waves-button-input')
            buttonSubmit.click
            
            $fluent_wait.until { driver.find_element(class: 'btn-message').displayed? }
            buttonAccept = driver.find_element(class: 'btn-message')
            buttonAccept.click
            
            $fluent_wait.until { driver.find_element(class: 'toolbar-avatar').displayed? }
            avatarButton = driver.find_element(class: 'toolbar-avatar')
            avatarButton.click

            $fluent_wait.until { driver.find_element(class: 'mat-list-item-avatar').displayed? }
            userDetailsButton = driver.find_element(class: 'mat-list-item-avatar')
            userDetailsButton.click

            $fluent_wait.until { driver.find_element(class: 'se-user-detail-container').displayed? }
        ensure
            driver.close
            reoprtFile.write '
                <html>
                    <head>
                        <meta charset="UTF-8">
                        <meta http-equiv="X-UA-Compatible" content="IE=edge">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Document</title>
                    </head>
                    <body>
                        <h1 style="color: green;">PASSED</h1>
                    </body>
                </html>
            '
        end
    end
end
