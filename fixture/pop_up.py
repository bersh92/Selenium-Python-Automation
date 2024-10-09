import time

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver


class PopUp:
    user_name_field = '#user_name'
    employee_name_field = '#selectedEmployee_value'
    password_field = '#password'
    confirm_password_field = '#confirmpassword'
    save_button = '#modal-save-button'
    user_exists_error_massage = "//span[text()='Already exists']"
    user_name_filter_field = '//input[@id="systemuser_uname_filter"]'
    filter_popup_table = '//div[@class="modal modal-fixed-footer open"]//h4[text()="Filter Users"]'
    filter_search_button = '//div[@class="modal modal-fixed-footer open"]//a[text()="Search"]'
    pass_required_message = '//input[@id="password"]/following::span[text()="Required"]'
    confirm_pass_required_message = '//input[@id="confirmpassword"]/following::span[text()="Required"]'
    pass_length_message = '//input[@id="password"]/following::span[text()="Your password should have at least 8 characters."]'
    pass_strength_message = '.password-strength-check'
    empty_space = '.password-help-text-container small'
    password_error_massage = '//input[@id="password"]/following-sibling::span'
    confirm_password_error_massage = '//input[@id="confirmpassword"]/following-sibling::span'
    strength_indicator = '.password-strength-check'
    autocomplete_dropdown = '#employee_name_filter_dropdown span.angucomplete-title'
    message_no_results = "//div[contains(text(),'No results found')]"
    ess_role_input_field = '#essroles_inputfileddiv input'
    ess_role_dropdown_values = '#essroles_inputfileddiv li'
    supervisor_role_input_field = '#supervisorroles_inputfileddiv input'
    supervisor_role_dropdown_values = '#supervisorroles_inputfileddiv li'
    location_input_field = '#location_inputfileddiv input'
    location_dropdown_values = '#location_inputfileddiv li'
    admin_role_input_field = '#adminroles_inputfileddiv input'
    admin_role_dropdown_values = '#adminroles_inputfileddiv li'
    status_input_field = '#status_inputfileddiv input'
    status_dropdown_values = '#status_inputfileddiv li'
    drop_down_is_expanded = 'input[class="select-dropdown active"]'
    filter_reset_button = '//div[@class="modal modal-fixed-footer open"]//a[text()="Reset"]'
    filter_cancel_button = '//div[@class="modal modal-fixed-footer open"]//a[text()="Cancel"]'
    searching_text = '//div[@id="employee_name_filter_dropdown"]/div[text()="Searching..."]'
    list_of_found_employee_names = '#employee_name_filter_dropdown div[ng-repeat="result in results"] span[class="angucomplete-title"]'
    list_of_drop_down_values = 'ul[id^="select-options"][style*="display: block"] li span'
    employment_status_drop_down = '//label[text()="Employment Status"]/preceding-sibling::div//input'
    location_drop_down = '//label[text()="Location"]/preceding-sibling::div//input'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.training_filter = TrainingFilter(step, wd)
        self.reportsAnalytics = ReportAnalytics(step, wd)

    def set_username(self, text):
        self.step.input_text(self.user_name_field, text)

    def set_employee_name(self, text):
        self.step.input_text(self.employee_name_field, text)
        self.step.specified_element_is_not_present(self.searching_text, 6)
        if self.step.specified_element_is_present(self.message_no_results, 3) == False:
            self.step.click_element_containing_text(self.list_of_found_employee_names, text)

    def set_password(self, text):
        self.step.click_on_element(self.password_field)
        self.step.input_text(self.password_field, text)

    def set_confirm_password(self, text):
        self.step.input_text(self.confirm_password_field, text)

    def click_on_save(self):
        self.step.click_on_element(self.save_button)

    def get_user_exist_error(self):
        return self.step.get_element_text(self.user_exists_error_massage)

    def click_on_search(self):
        self.step.click_on_element(self.filter_search_button)

    def get_strength_indicator_text(self):
        self.step.specified_element_is_present(self.strength_indicator, 5)
        time.sleep(0.5)
        return self.step.get_element_text(self.strength_indicator)

    def get_password_error(self):
        return self.step.get_element_text(self.password_error_massage)

    def get_confirm_password_error(self):
        return self.step.get_element_text(self.confirm_password_error_massage)

    def get_autocomplete_names(self):
        return self.step.get_elements_texts(self.autocomplete_dropdown)

    def get_no_results_message(self):
        return self.step.get_element_text(self.message_no_results)

    def get_ess_role_dropdown_values(self):
        return self.step.get_elements_texts(self.ess_role_dropdown_values)

    def get_admin_role_dropdown_values(self):
        return self.step.get_elements_texts(self.admin_role_dropdown_values)

    def get_supervisor_role_dropdown_values(self):
        return self.step.get_elements_texts(self.supervisor_role_dropdown_values)

    def get_status_dropdown_values(self):
        return self.step.get_elements_texts(self.status_dropdown_values)

    def get_location_dropdown_values(self):
        return self.step.get_elements_texts(self.location_dropdown_values)

    def get_ess_role_selected_dropdown_value(self):
        return self.step.get_element_attribute_value(self.ess_role_input_field, 'value', True)

    def get_admin_role_selected_dropdown_value(self):
        return self.step.get_element_attribute_value(self.admin_role_input_field, 'value', True)

    def get_supervisor_role_selected_dropdown_value(self):
        return self.step.get_element_attribute_value(self.supervisor_role_input_field, 'value', True)

    def get_status_selected_dropdown_value(self):
        return self.step.get_element_attribute_value(self.status_input_field, 'value', True)

    def get_location_selected_dropdown_value(self):
        return self.step.get_element_attribute_value(self.location_input_field, 'value', True)

    def set_ess_role_input_dropdown(self, text):
        self.step.click_on_element(self.ess_role_input_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.ess_role_dropdown_values, text)

    def set_admin_role_input_dropdown(self, text):
        self.step.click_on_element(self.admin_role_input_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.admin_role_dropdown_values, text)

    def set_supervisor_role_dropdown(self, text):
        self.step.click_on_element(self.supervisor_role_input_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.supervisor_role_dropdown_values, text)

    def set_status_input_dropdown(self, text):
        self.step.click_on_element(self.status_input_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.status_dropdown_values, text)

    def set_location_input_dropdown(self, text):
        self.step.click_on_element(self.location_input_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.location_dropdown_values, text)

    def click_on_filter_reset_button(self):
        self.step.click_on_element(self.filter_reset_button)

    def click_on_filter_cancel_button(self):
        self.step.click_on_element(self.filter_cancel_button)

    def wait_filter_pop_up_stop_displayed(self):
        self.step.specified_element_is_not_present(self.filter_popup_table)

    def set_employment_status(self, text):
        self.step.click_on_element(self.employment_status_drop_down)
        time.sleep(1)
        self.step.click_element_by_text(self.list_of_drop_down_values, text)

    def set_location(self, text):
        self.step.click_on_element(self.location_drop_down, True)
        time.sleep(1)
        self.step.click_element_containing_text(self.list_of_drop_down_values, text)

    def set_hr_administration_drop_downs(self, user_name=None, employee_name=None, ess_role=None):
        if user_name is not None:
            self.set_username(user_name)
        if employee_name is not None:
            self.set_employee_name(employee_name)
        if ess_role is not None:
            self.set_ess_role_input_dropdown(ess_role)

class ReportAnalytics:
    add_folder_header = '//p[text()="Add Folder"]'
    add_folder_input_field = 'input[placeholder="Enter Folder Name"]'
    save_button = '//div[text()="Save"]'
    folder_success_save_message = '//div[@class="oxd-toast-content oxd-toast-content--success"]/p'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def input_new_folder_name(self, text):
        self.step.wait_for_element(self.add_folder_header)
        self.step.input_text(self.add_folder_input_field, text)

    def click_on_save_button(self):
        self.step.click_on_element(self.save_button, True)

class TrainingFilter:
    title_field = 'div[class="input-field row"] #searchCourse_title'
    iframe = "#noncoreIframe"

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def set_title(self, title):
        self.step.switch_to_iframe(self.iframe)
        self.step.input_text(self.title_field, title)
        self.step.switch_to_default_content()