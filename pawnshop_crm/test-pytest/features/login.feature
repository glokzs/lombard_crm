Feature: Login as admin
  A sample test
  
Scenario: Login as admin
    Given Login page
#    Then Create superuser
    Then I logging as admin
    Then Click on user model
#     I should see admin page
