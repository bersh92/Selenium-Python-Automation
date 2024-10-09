from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

from fixture.table import Table


class EmployeeManagement:
    home_button = "a[data-automation-id='menu_home']"
    list_of_widgets_header_texts = ".widget-header span:last-child"
    filter_button = '*[data-tooltip="Filter"]'
    employee_management_table_loading_spinner = '#loading-bar .bar .peg'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.table = Table(step,
                           row_selector='#content tbody tr',
                           column_selectors={'user_icon': 'td:nth-child(1)',
                                             'employee_id': 'td:nth-child(2)',
                                             'name': 'td:nth-child(3)',
                                             'job_title': 'td:nth-child(4)',
                                             'employment_status': 'td:nth-child(5)',
                                             'sub_unit': 'td:nth-child(6)',
                                             'cost_center': 'td:nth-child(7)',
                                             'location': 'td:nth-child(8)',
                                             'supervisor': 'td:nth-child(9)'})

    def click_home(self):
        self.step.click_on_element(self.home_button)

    def get_widgets_headers(self):
        return self.step.get_elements_texts(self.list_of_widgets_header_texts)

    def click_on_filter(self):
        self.step.click_on_element(self.filter_button, 1)

    def wait_for_loading_bar_gone(self):
        self.step.specified_element_is_not_present(self.employee_management_table_loading_spinner, 10)