
# Project Setup and Testing Guide

This guide covers the setup process for running automated tests in the project, generating reports with Allure, and configuring PyCharm for test execution.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [PyCharm Run Configurations](#pycharm-run-configurations)
- [Running Tests from the Console](#running-tests-from-the-console)
- [Parallel Execution](#parallel-execution)
- [Running Specific Tests](#running-specific-tests)
- [Logging Levels](#logging-levels)
- [Opening Allure Reports](#opening-allure-reports)

## Prerequisites

- Python 3.x
- PyCharm or any other IDE/Text Editor

## Installation

### Install Required Packages

Install all required packages listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

### Install Allure Command Line

- **macOS**: Install Allure using Homebrew with the following command:

```bash
brew install allure
```

- **Windows**:

1. Download the latest Allure Commandline zip from the [Allure Releases Page](https://github.com/allure-framework/allure2/releases).
2. Unzip the contents to a directory (e.g., `C:\Allure`).
3. Add the `bin` directory from the unzipped location to your system's PATH environment variable.

## PyCharm Run Configurations

Set up run configurations in PyCharm to easily run tests and open reports:

1. Open PyCharm and navigate to `Run` > `Edit Configurations`.
2. Click the `+` button to add a new Python configuration.
3. Name the configuration (e.g., "Run All Tests").
4. Script path: Choose the path to your `runner.py` script.
5. Parameters: Enter the specific command (e.g., `test`, `testHeadless`, or `openReport`).
6. Repeat steps 2-5 to create configurations for `testHeadless` and `openReport`.

**Important:** Tests executed by clicking the run button in the IDE do **not** generate HTML reports by default.

## Running Tests from the Console

Besides using PyCharm configurations, you can run tests directly from the console using `runner.py`.

### Basic Usage

**Run tests in normal mode:**
```bash
python runner.py testNormal
```

**Run tests in headless mode:**
```bash
python runner.py testHeadless
```

**Open Allure HTML Report:**
```bash
python runner.py openReport
```

## Parallel Execution

**Run tests in parallel:**
```bash
python runner.py testNormal --parallel
python runner.py testHeadless --parallel
```

**Run tests in parallel, filtering by specific groups:**
```bash
python runner.py testNormal --parallel --group=group1
python runner.py testHeadless --parallel --group=group1
```

## Running Specific Tests

**Run a specific test file in normal mode:**
```bash
python runner.py testNormal --test=test/test_case_1_Login_to_the_application.py
```

**Run a specific test file in headless mode:**
```bash
python runner.py testHeadless --test=test/test_case_1_Login_to_the_application.py
```

## Logging Levels

In pytest, the logging levels are typically the same as those defined in the Python `logging` module. Here's a list of the standard logging levels in increasing order of severity:

1. **DEBUG**: Detailed information, typically of interest only when diagnosing problems.
2. **INFO**: Confirmation that things are working as expected.
3. **WARNING**: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., 'disk space low'). The software is still working as expected.
4. **ERROR**: Due to a more serious problem, the software has not been able to perform some function.
5. **CRITICAL**: A serious error, indicating that the program itself may be unable to continue running.

## Opening Allure Reports

After running tests, Allure reports can be opened directly from the terminal.

### To open the report:
1. After executing tests, generate the report by running:
   ```bash
   python runner.py openReport
   ```

This command will automatically open the Allure report in your default browser.
