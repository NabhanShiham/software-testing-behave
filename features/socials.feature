Feature: Saucedemo Social Links

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login' button is clicked

  Scenario Outline: Clicking Social Network Links
    Given the '<sns>' link is clicked
    Then the correct '<webpage>' is displayed
    Examples:
    |sns|webpage|
    |Twitter   |https://x.com/saucelabs|
    |Facebook    |https://www.facebook.com/saucelabs |
    |LinkedIn   |https://www.linkedin.com/company/sauce-labs/|