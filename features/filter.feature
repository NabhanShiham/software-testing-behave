Feature: Saucedemo Product Filter

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login' button is clicked

  Scenario Outline: Sorting Products by filters
    Given the filter is set to '<filter_by>'
    Then the first product should be '<product>'
    Examples:
    |filter_by|product|
    |az         | Sauce Labs Backpack     |
    |za           |Test.allTheThings() T-Shirt (Red)|
    |lohi             |Sauce Labs Onesie            |
    |hilo                 |Sauce Labs Fleece Jacket |