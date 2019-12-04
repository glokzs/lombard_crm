Feature: Operations

Scenario: Operations
    Given Client
    And Client document
    And Category
    And Subcategory
    And Loan
    And PledgeItem
    And Create superuser
    And Login page
    Then I logging as user
    And I click "Займы"
    And I should see test loan
    And click on test loan
    And I should see detail loan page
    And I click on "Продление"
    And I should see and fill in prolongation loan option
    And I click close loan option
    And I click close button
    And I click to the "Журнал операций"
    And I should see list of made operations
