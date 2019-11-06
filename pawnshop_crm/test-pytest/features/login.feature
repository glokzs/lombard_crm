Feature: Login as admin
  A sample test
  
Scenario: Login as admin
    Given Create superuser
    And Login page
    Then I logging as admin
    Then I should see admin page
    Then I click "Пользователи"
    Then I should see "Выберите пользователь для изменения"
    Then I click "Добавить пользователя"
    Then I should see user create menu
    Then I enter new user info
    Then I should see user successful creation
