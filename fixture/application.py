import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from assertpy import assert_that

from fixture.demonstration_app_demo_qa import DemonstrationAppDemoQa
from fixture.orange_hrm import OrangeHrm
from fixture.step import StepHelper
from helpers.utils import Utils


class Application:
    def __init__(self, headless=False):
        # Set the root directory of the project
        project_root = Utils.get_project_root()
        # Set up ChromeDriver service to suppress logs by setting its output to dev/null
        log_path = os.path.devnull
        service = Service(log_path=log_path)

        # Set up Chrome options
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-notifications")
        # User agent can be customized as needed, but default Chrome user agent is usually sufficient
        # chrome_options.add_argument("user-agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'")

        # Set up download directory
        project_root = Utils.get_project_root()
        download_path = os.path.join(project_root, 'files', 'download')

        if not os.path.exists(download_path):
            os.makedirs(download_path)

        prefs = {
            "download.default_directory": download_path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        }
        chrome_options.add_experimental_option("prefs", prefs)

        self.wd = webdriver.Chrome(service=service, options=chrome_options)
        # self.wd.set_window_size(1920, 1080)  # Optionally setting window size; consider if necessary

        # Setup other application components
        self.assert_that = assert_that
        self.step = StepHelper(self)
        self.orangeHrm = OrangeHrm(self)
        self.demonstrationAppDemoQa = DemonstrationAppDemoQa(self)
        self.utils = Utils()

    def destroy(self):
        # Ensure the web driver quits properly
        if self.wd:
            self.wd.quit()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.destroy()
