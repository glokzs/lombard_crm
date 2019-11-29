Feature: Create loan
  A sample test

Scenario: Create loan
    Given Create superuser
    And Login page
    Then I logging as user
    Then I should see index page
    Then I click "Займы"
    Then I should see "Список кредитов"
    Then I click "Добавить операцию"
    Then I should see "Выбор клиента"
    Then I click on client
    Then I click to choose client
    Then I should see "Добавить займ"
    Then I click "Добавить залоговое имущество"
    Then I should see "Добавить залоговое имущество"
    Then I add loan item
