# Global
require './global/settings.rb'
require './global/wait.rb'

# Test
require './tests/login_success.rb'
require './tests/login_wrong_inputs.rb'

LoginSuccess.run
# LoginWrongInputs.run
