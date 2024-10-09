import os
import time

from selenium.webdriver.remote.webdriver import WebDriver

from fixture.calendar import Calendar, CalendarType
from fixture.step import StepHelper
from helpers.utils import Utils


class RecruitmentAts:
    add_candidate_button = 'button[tooltip="Add Candidate"]'
    page_loading_animation = 'div[class="oxd-skeleton --animate"]'
    message_of_successful_action = '//div[contains(@class, "oxd-toast-content")]//p[2]'
    search_input_field = '//input[@placeholder="Search"][@data-test="autocompleteSelect"]'
    search_field_spinner = '//div[text()="Searching..."]'
    search_autocomplete_dropdowns = '.oxd-autocomplete-option span'
    download_button = 'button[tooltip="Export to CSV"]'
    progress_loading_bar = 'div[class="progress-bar-modal"]'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.calendar = Calendar(self.step, CalendarType.OXD)

    def wait_for_page_load(self):
        self.step.specified_element_is_not_present(self.page_loading_animation, 20)

    def click_on_add_candidate_button(self):
        self.step.click_on_element(self.add_candidate_button)

    def get_action_message_text(self):
        self.step.wait_for_element(self.message_of_successful_action, 10)
        return self.step.get_element_text(self.message_of_successful_action)

    def set_search(self, text):
        self.step.input_text(self.search_input_field, text)
        self.step.wait_for_element(self.search_field_spinner, 5)
        self.step.specified_element_is_not_present(self.search_field_spinner, 15)
        self.step.click_element_containing_text(self.search_autocomplete_dropdowns, text)

    def export_to_csv(self):
        self.step.click_on_element(self.download_button)
        # Wait for the download to complete (you may need to adjust the sleep duration)
        self.step.specified_element_is_not_present(self.page_loading_animation, 20)
        time.sleep(3)  # Additional sleep to ensure download completes
        # Check the download directory for the downloaded file
        download_path = os.path.join(Utils.get_project_root(), 'files', 'download')
        downloaded_files = os.listdir(download_path)
        if len(downloaded_files) == 0:
            raise Exception("No files were downloaded.")