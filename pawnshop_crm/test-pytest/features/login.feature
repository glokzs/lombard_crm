Feature: Login as admin
  A sample test
  
Scenario: Login as admin
    Given Create superuser
    And Login page
    Then I login as admin
    And I should see admin page
    And I click "Пользователи"
    And I should see "Выберите пользователь для изменения"
    And I click "Добавить пользователя"
    And I should see user create menu
    And I enter new user info
    And I should see user successful creation
