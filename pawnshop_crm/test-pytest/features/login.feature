Feature: Login as admin
  A sample test
  
Scenario: Login as admin
    Given Create superuser
    And Login page
    Then I logging as admin
    Then I should see admin page
    Then I click "Пользователи"
    And I should see "Выберите пользователь для изменения"

