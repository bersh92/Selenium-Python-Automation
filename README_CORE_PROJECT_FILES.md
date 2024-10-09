# UI Automation Framework

This repository contains a UI automation framework designed to facilitate the automated testing of web applications using Python and pytest. It includes capabilities such as generating test reports and taking screenshots during test execution.

## Table of Contents

- [conftest.py](#conftestpy)
- [runner.py](#runnerpy)
- [pytest.ini](#pytestini)
- [application.py](#applicationpy)
- [step.py](#steppy)

## conftest.py

`conftest.py` contains shared fixture functions utilized across multiple test files, recognized automatically by pytest.

### Key Features:
- **Browser Fixture**: Manages the setup and teardown of web browsers. Configurable for different browsers and settings.
- **Screenshot Utility**: Captures screenshots in case of test failures.
- **Allure Reporting**: Integrates with Allure to generate detailed test reports.

## runner.py

`runner.py` serves as the entry point for running tests, handling test environment configuration, test collection, and execution.

### Key Features:
- **Test Discovery and Execution**: Identifies and runs tests, with options for executing specific tests or groups.
- **Command-Line Options**: Supports various options like `--group`, `--test-name`, `--parallel`, and `--headless` for custom test executions.

## pytest.ini

`pytest.ini` configures pytest, dictating test discovery and execution behavior. It provides a way to set default test behaviors, like skipping certain tests unless specified.

### Key Features:
- **Test Patterns and Custom Markers**: Configures patterns for test discovery and defines custom markers for test execution.
- **Adaptable Configuration**: Can be extended to include new markers or options as required for specific testing needs.

## application.py

`application.py` sets up the application context and initializes settings required for the tests.

### Key Features:
- **Application Configuration Management**: Handles settings for different testing environments.
- **Utility Functions**: Provides common utilities like logging and configuration parsing.

## step.py

`step.py` provides a collection of helper methods designed to streamline interactions with web elements during UI automation. These methods simplify operations such as locating elements, interacting with dropdowns, handling JavaScript-based actions, and performing assertions on UI components.

### Key Features:
- **Element Locators**: Functions for locating elements using XPath and CSS selectors.
- **Element Interactions**: Methods for clicking elements, inputting text, selecting dropdown values, and interacting with visible elements.
- **Element Presence Validation**: Utility methods to check if elements are present or absent from the DOM.
- **Advanced Features**: Includes methods for handling JavaScript-based clicks, switching between browser tabs or iframes, and performing scrolling actions.
- **Assertions**: A helper function for comparing lists and reporting differences in test results.
  
### Usage Examples:
- **Clicking an Element**: 
  ```python
  step_helper.click_on_element("//button[@id='submit']")
