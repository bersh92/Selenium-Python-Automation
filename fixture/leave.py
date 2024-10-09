
from fixture.calendar import Calendar, CalendarType
from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver


class Leave:
    selector_example = "//div[@id='systemUserDiv'] //*[text()='add']"

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.calendar = Calendar(self.step, CalendarType.DEFAULT)

    def method_example(self):
        pass