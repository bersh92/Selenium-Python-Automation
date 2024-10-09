import subprocess
import sys
import os
import shutil

if os.name == 'nt':  # Windows
    ALLURE_COMMAND_PATH = r'C:\allure-2.27.0\bin\allure.bat'
else:  # Assume Linux or macOS
    ALLURE_COMMAND_PATH = 'allure'


def clear_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)
    os.makedirs(directory)


def open_allure_report():
    report_dir = "allure-report"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    subprocess.call([ALLURE_COMMAND_PATH, 'serve', 'allure-results'])


def generate_allure_report():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    results_dir = os.path.join(base_dir, "allure-results")
    report_dir = os.path.join(base_dir, "allure-report")
    subprocess.call([ALLURE_COMMAND_PATH, 'generate', results_dir, '-o', report_dir, '--clean'])


def run_tests_and_generate_report(headless=False, parallel=False, group=None, test_name=None):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    results_dir = os.path.join(base_dir, "allure-results")
    clear_directory(results_dir)
    clear_directory(os.path.join(base_dir, "allure-report"))

    pytest_cmd = ['pytest']
    if test_name:
        # Use only test_name which should include the full path to the test
        pytest_cmd.append(test_name)
    else:
        # Use the default test directory if no specific test is specified
        pytest_cmd.append('test/')

    if headless:
        pytest_cmd.append('--headless')
    if parallel:
        pytest_cmd += ['-n3', '--dist=loadscope']
    if group:
        pytest_cmd.append(f'-m {group}')
    pytest_cmd.append('--alluredir=allure-results')
    # pytest_cmd.append('-v')  # Add verbose output

    print("Executing command:", ' '.join(pytest_cmd))
    result = subprocess.call(pytest_cmd)

    if result != 0:
        sys.exit(result)  # Exit with the same status code as pytest if tests fail

    if not test_name:
        generate_allure_report()


if __name__ == '__main__':
    command = sys.argv[1] if len(sys.argv) > 1 else None
    headless = '--headless' in sys.argv
    parallel = '--parallel' in sys.argv
    group = None
    test_name = None

    # Further parsing for group, test, or other parameters
    for arg in sys.argv[2:]:
        if arg.startswith('--group='):
            group = arg.split('=')[1]
        elif arg.startswith('--test='):
            test_name = arg.split('=')[1]

    if command == 'openReport':
        open_allure_report()
    elif command == 'testHeadless':
        run_tests_and_generate_report(headless=True, parallel=parallel, group=group, test_name=test_name)
    elif command == 'testNormal':
        run_tests_and_generate_report(headless=False, parallel=parallel, group=group, test_name=test_name)
