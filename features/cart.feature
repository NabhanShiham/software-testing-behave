Feature: Saucedemo Shopping Cart

  Background:
    Given the home page is opened
    And the 'Username' field is filled with 'standard_user'
    And the 'Password' field is filled with 'secret_sauce'
    And the 'Login' button is clicked

  Scenario Outline: Removing products from the cart
    Given the '<product>' is added to the cart
    And the 'Cart' button is clicked
    When the '<product>' is removed from the cart
    Then the cart does not contain anything
    Examples:
        | product                           |
        | Sauce Labs Onesie                 |
        | Sauce Labs Bolt T-Shirt           |
        | Test.allTheThings() T-Shirt (Red) |
        | Sauce Labs Backpack               |
        | Sauce Labs Fleece Jacket          |
        | Sauce Labs Bike Light             |

  Scenario Outline: Removing just one product from the cart
    Given the '<product1>' is added to the cart
    And the '<product2>' is added to the cart
    And the '<product3>' is added to the cart
    And the 'Cart' button is clicked
    When the '<product3>' is removed from the cart
    Then the cart should contain 2 products
    # to clear the cart
    And the '<product1>' is removed from the cart
    And the '<product2>' is removed from the cart
    Examples:
      |product1                            |product2                       |product3                           |
      | Sauce Labs Onesie                  | Sauce Labs Bolt T-Shirt       | Test.allTheThings() T-Shirt (Red) |
      | Sauce Labs Bolt T-Shirt            | Sauce Labs Onesie             | Sauce Labs Backpack               |
      | Sauce Labs Backpack                |   Sauce Labs Bike Light       |Sauce Labs Fleece Jacket           |
      | Test.allTheThings() T-Shirt (Red)  | Sauce Labs Onesie             |  Sauce Labs Bolt T-Shirt          |

  Scenario Outline: Navigating to cart and continuing to shop
    Given the '<product1>' is added to the cart
    And the '<product2>' is added to the cart
    And the 'Cart' button is clicked
    And the 'Continue Shopping' button is clicked
    And the '<product3>' is added to the cart
    And the 'Cart' button is clicked
    Then the cart should contain 3 products
    # to clear the cart
    And the '<product1>' is removed from the cart
    And the '<product2>' is removed from the cart
    And the '<product3>' is removed from the cart
    Examples:
      |product1                            |product2                       |product3                           |
      | Sauce Labs Onesie                  | Sauce Labs Bolt T-Shirt       | Test.allTheThings() T-Shirt (Red) |
      | Sauce Labs Bolt T-Shirt            | Sauce Labs Onesie             | Sauce Labs Backpack               |
      | Sauce Labs Backpack                |   Sauce Labs Bike Light       |Sauce Labs Fleece Jacket           |
      | Test.allTheThings() T-Shirt (Red)  | Sauce Labs Onesie             |  Sauce Labs Bolt T-Shirt          |

