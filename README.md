# SauceDemo Test Automation Project with Behave

## Project Description
This project automates the testing of key functionalities of the SauceDemo e-commerce website using **Selenium WebDriver** and **Behavior-Driven Development (BDD)** principles implemented with the **Behave** framework.

The tests cover various scenarios such as user login, product filtering, shopping cart operations, purchasing products, and verifying social media links.

## Features Tested
1. **Login**
   - Correct and incorrect login attempts.
   - Logging out functionality.
2. **Shopping Cart**
   - Adding and removing products.
   - Verifying cart contents.
3. **Shopping**
   - Purchasing single, multiple, and all products.
   - Validating the total price.
4. **Product Filtering**
   - Sorting products using different filters.
5. **Social Media Links**
   - Verifying correct navigation to social media pages.

## Project Structure
```
|-- features
|   |-- login.feature
|   |-- cart.feature
|   |-- shopping.feature
|   |-- filter.feature
|   |-- socials.feature
|   |-- environment.py
|
|-- features/steps
|   |-- login.py
|   |-- cart.py
|   |-- shopping.py
|   |-- filter.py
|   |-- socials.py
|
|-- features/pages
|   |-- homepage.py
|   |-- login_page.py
|   |-- cart_page.py
|
|-- main.py
|-- README.md
```

### Description of Files
- **`features`**: Contains all the feature files describing the test scenarios in Gherkin syntax.
- **`steps`**: Contains step definitions for each feature file.
- **`pages`**: Contains Page Object Model (POM) implementations for the tested web pages.

## Prerequisites
Ensure the following are installed:
- Python (>= 3.10)
- Firefox web browser and Geckodriver (compatible versions)
- Selenium WebDriver
- Behave framework

## Running the Tests
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd saucedemo-testing-with-behave
   ```

2. Run all tests:
   ```bash
   behave
   ```

3. Run tests for a specific feature:
   ```bash
   behave features/login.feature
   ```

## Test Execution Summary
- **Login**:
  - Verifies valid and invalid login attempts.
  - Ensures users can log out successfully.
- **Shopping Cart**:
  - Tests adding and removing products.
  - Validates cart contents dynamically.
- **Shopping**:
  - Tests purchasing different combinations of products.
  - Verifies price calculations.
- **Product Filtering**:
  - Confirms product sorting functionality.
- **Social Media Links**:
  - Ensures correct navigation to SauceDemo's social media pages.

## Notes
- Test data is pre-defined in the feature files.
- This project is designed for SauceDemo's test environment and may not work with other e-commerce sites.

## Author
- **Mohamed Nabhan Shiham**
- Contact: [nabhanshiham@gmail.com](mailto:nabhanshiham@gmail.com)

