# Selenium Python Project – Page Object Model Automation

##  Overview
This repository is a personal Selenium automation project in Python, structured using the **Page Object Model (POM)** design pattern. It includes automated test scripts for common features in a web application, such as login, product selection, and cart functionality.

---

##  Project Structure

selenium-python-project/
├── pageObjects/ # Contains POM classes (e.g., LoginPage, ProductPage, CartPage)
├── tests/ # Test script files using POM classes
│ ├── loginTest.py
│ ├── productTest.py
│ ├── cartTest.py
│ └── testRunner.py # Master test runner
├── .gitignore
└── README.md


---

##  Usage Guide

1. **Clone repository:**
   git clone https://github.com/Vinna28/selenium-python-project.git
   cd selenium-python-project
2. **Install dependencies (recommended via pip):**
  pip install selenium
3. **Run all tests:**
  python testRunner.py
  Or run tests individually:
  python tests/loginTest.py

Page Object Model (POM) Design
This project follows the POM pattern by separating:
Page classes (pageObjects/) that encapsulate element locators and interaction methods.
Test scripts (tests/) that import page classes to execute test flows.

Advantages of POM:
Better code readability and maintenance.
Reusable page methods across multiple tests.
Easier updates when UI elements change.

What I Learned / Implemented
Design and implement Page Object Model in Selenium with Python.
Structure test suites for login, product browsing, and cart management.
Centralize driver setup and teardown using testRunner.py.
Handle locators and UI interactions efficiently using reusable methods.

Next Steps / Enhancements
Add reporting (e.g., HTML or Allure reports) for cleaner test summaries.
Integrate with CI/CD services (e.g., GitHub Actions) to auto-run tests on commits.
Implement data-driven testing using JSON, CSV, or Excel for parameterized scenarios.
Introduce cross-browser testing (Chrome, Firefox, etc.).
Handle dynamic elements with improved wait strategies (explicit wait, retry logic).

Manual Run Example
Below is what running all tests might look like:
$ python testRunner.py
[INFO] Starting Selenium tests...
LoginTest: Passed
ProductTest: Passed
CartTest: Failed (Product not added)
[INFO] Tests completed. Check logs and screenshots (if implemented).

License & Credits
This project is licensed under the MIT License. Feel free to explore, adapt, or build upon it.
