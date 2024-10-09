import time

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

from fixture.table import Table


class HrAdministration:
    add_user_button = "//div[@id='systemUserDiv'] //*[text()='add']"
    filter_users_button = '#ribbon-actions ui-view a'
    filtered_usernames = 'tbody td:nth-child(2) span'
    filtered_user_roles = 'tbody td:nth-child(3) span'
    filter_no_records_message = '//div[text()="No Records Found"]'
    save_button = '#modal-save-button'
    filter_popup_table = '//div[@class="modal modal-fixed-footer open"]//h4[text()="Filter Users"]'
    first_table_row = '#systemUserDiv tbody tr:nth-child(1)'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.table = Table(step,
                           row_selector='#systemUserDiv tbody tr',
                           column_selectors={'check_box': 'td:nth-child(1)',
                                             'user_name': 'td:nth-child(2)',
                                             'user_role': 'td:nth-child(3)'})

    def wait_for_table(self):
        self.step.wait_for_element(self.first_table_row, 40)

    def click_add_user(self):
        self.step.wait_for_element(self.first_table_row, 40)
        self.step.click_on_element(self.add_user_button)

    def click_on_filter(self):
        self.step.wait_for_element(self.first_table_row, 40)
        self.step.click_on_element(self.filter_users_button, 1)

    def get_list_of_user_names(self):
        time.sleep(3)
        return self.step.get_elements_texts(self.filtered_usernames)

    def get_filter_no_records_message_text(self):
        return self.step.get_element_text(self.filter_no_records_message)

    def is_list_of_users_displayed(self):
        self.step.specified_element_is_not_present(self.filter_no_records_message, 5)
        return self.step.specified_element_is_present(self.filtered_usernames)
