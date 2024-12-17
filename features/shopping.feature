Feature: Saucedemo Shopping for products

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login' button is clicked

  Scenario: Buying a bike light
    Given the 'Sauce Labs Bike Light' is added to the cart
    And the 'Cart' button is clicked
    And the 'Checkout' button is clicked
    And the 'First Name' field is filled with 'test_first'
    And the 'Last Name' field is filled with 'test_last'
    And the 'Zip Code' field is filled with '2003'
    When the 'Continue' button is clicked
    Then the price should read 'Total: $10.79'
    And the 'Finish' button is clicked
    And the 'Back Home' button is clicked

  Scenario: Buying a bike light and a fleece jacket
    Given the 'Sauce Labs Bike Light' is added to the cart
    And the 'Sauce Labs Fleece Jacket' is added to the cart
    And the 'Cart' button is clicked
    And the 'Checkout' button is clicked
    And the 'First Name' field is filled with 'test_first'
    And the 'Last Name' field is filled with 'test_last'
    And the 'Zip Code' field is filled with '2003'
    When the 'Continue' button is clicked
    Then the price should read 'Total: $64.78'
    And the 'Finish' button is clicked
    And the 'Back Home' button is clicked

  Scenario: Buying everything on the website
    Given everything is added to the cart
    And the 'Cart' button is clicked
    And the 'Checkout' button is clicked
    And the 'First Name' field is filled with 'test_first'
    And the 'Last Name' field is filled with 'test_last'
    And the 'Zip Code' field is filled with '2003'
    When the 'Continue' button is clicked
    Then the price should read 'Total: $140.34'
    And the 'Finish' button is clicked
    And the 'Back Home' button is clicked

  Scenario: Buying nothing
    Given the 'Cart' button is clicked
    And the 'Checkout' button is clicked
    And the 'First Name' field is filled with 'test_first'
    And the 'Last Name' field is filled with 'test_last'
    And the 'Zip Code' field is filled with '2003'
    When the 'Continue' button is clicked
    Then the price should read 'Total: $0.00'
    And the 'Finish' button is clicked
    And the 'Back Home' button is clicked


