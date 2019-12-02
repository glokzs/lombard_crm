Feature: Create client
  A sample test

  Scenario: Create client
    Given Create superuser
    And Login page
    Then I logging as user
    Then I should see index page
    Then I click "Займы"
    Then I should see "Список кредитов"
    Then I click "Добавить операцию"
    Then I should see "Выбор клиента"
    Then I enter new client info
    Then I should see "Добавить документ"
    Then I enter client document info
    Then I should see test client
