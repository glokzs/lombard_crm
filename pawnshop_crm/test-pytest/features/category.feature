Feature: Create category and subcategory
   Category, tariffs and subcategory test

  Scenario: Create category
    Given Create superuser
    And Login page
    Then I login as admin
    And I should see admin page
    And I click on Category option
    And I should see Category list
    And I click creation option
    And I should see form
    And I filling name and tariff and save form
    And I should see Category list and success message
    And I click main admin menu
    And I should see admin page
    And I click subcategory option
    And I should see subcategory menu
    And I click create subcategory option
    And I should see create subcategory form
    And I filling form and click save
    And I should see success creation page
