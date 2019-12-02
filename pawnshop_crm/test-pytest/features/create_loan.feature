Feature: Create client, category and subcategory and after create loan
   Category, tariffs and subcategory test

Scenario: Create loan
    Given Client
    And Client document
    And Category
    And Subcategory
    And Create superuser
    And Login page
    Then I logging as user
    And I should see index page
    And I click "Займы"
    And I should see "Список кредитов"
    And I click "Добавить операцию"
    And I should see "Выбор клиента"
    And I click on client
    And I click to choose client
    And I should see "Добавить займ"
    And I click "Добавить залоговое имущество"
    And I should see "Добавить залоговое имущество"
    And I add loan item
    And I should see "Добавить займ"
    And I add loan sum, duration, warranty period
    And I should see "Кредит"
    And I click on "Выкуп"