import os

from fixture.employee_management import EmployeeManagement
from fixture.hr_administration import HrAdministration
from fixture.leave import Leave
from fixture.pop_up import PopUp
from fixture.recruitment_ats import RecruitmentAts
from fixture.side_menu import SideMenu
from fixture.step import StepHelper
from dotenv import load_dotenv

load_dotenv()


class OrangeHrm:
    username_field = 'input[id="txtUsername"]'
    password_field = 'input[id="txtPassword"]'
    login_button = 'button[type="submit"]'
    header = 'li[data-tooltip="Employee Management"] div'
    username_error_message = 'span[id="txtUsername-error"]'
    password_error_message = 'span[id="txtPassword-error"]'

    def __init__(self, app):
        self.app = app
        self.step: StepHelper = self.app.step
        self.wd = self.app.wd
        self.sideMenu = SideMenu(self.step, self.wd)
        self.hrAdministration = HrAdministration(self.step, self.wd)
        self.popUp = PopUp(self.step, self.wd)
        self.employeeManagement = EmployeeManagement(self.step, self.wd)
        self.recruitmentAts = RecruitmentAts(self.step, self.wd)
        self.leave = Leave(self.step, self.wd)

    def openUrl(self, url="https://portnov01-trials713.orangehrmlive.com"):
        self.wd.get(url)

    def set_username(self, username):
        self.step.input_text(self.username_field, username)

    def set_password(self, password):
        self.step.input_text(self.password_field, password)

    def click_login_button(self):
        self.step.click_on_element(self.login_button)

    def login_to_the_application(self, username=None, password=None):
        if username is None:
            username = os.getenv('USERNAME_TEST')
        if password is None:
            password = os.getenv('PASSWORD')
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()

    def get_username_error(self):
        return self.step.get_element_text(self.username_error_message)

    def get_password_error(self):
        return self.step.get_element_text(self.password_error_message)

    def get_header_text(self):
        return self.step.get_element_text(self.header)

    def open_application_and_login(self):
        self.openUrl()
        self.login_to_the_application()
        self.app.assert_that(self.app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
