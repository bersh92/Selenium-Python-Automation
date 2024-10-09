import time
from enum import Enum

class CalendarType(Enum):
    DEFAULT = "default"
    OXD = "oxd"

class Calendar:
    def __init__(self, step_helper, calendar_type=CalendarType.DEFAULT):
        self._step = step_helper
        self._wd = self._step.wd
        self._calendar_type = calendar_type
        self._set_selectors()

    def _set_selectors(self):
        if self._calendar_type == CalendarType.DEFAULT:
            self._parent_selector = '//div[@aria-hidden="false"]//div[contains(@class, "picker__holder")]'
            self._year_dropdown_trigger = f'{self._parent_selector}//div[contains(@class, "picker__select--year")]/input'
            self._year_options = f'{self._parent_selector}//ul[contains(@class, "select-dropdown") and contains(@class, "active")]/li/span'
            self._month_dropdown_trigger = f'{self._parent_selector}//div[contains(@class, "picker__select--month")]/input'
            self._month_options = f'{self._parent_selector}//ul[contains(@class, "select-dropdown") and contains(@class, "active")]/li/span'
            self._day_picker = f'{self._parent_selector}//div[contains(@class, "picker__day")]'
        elif self._calendar_type == CalendarType.OXD:
            self._parent_selector = '.oxd-calendar-wrapper'
            self._year_dropdown_trigger = f'{self._parent_selector} .oxd-calendar-selector-year .oxd-calendar-selector-year-selected'
            self._year_options = f'{self._parent_selector} .oxd-calendar-dropdown li'
            self._month_dropdown_trigger = f'{self._parent_selector} .oxd-calendar-selector-month .oxd-calendar-selector-month-selected'
            self._month_options = f'{self._parent_selector} .oxd-calendar-dropdown li'
            self._day_picker = f'{self._parent_selector} .oxd-calendar-date'
        else:
            raise ValueError("Unknown calendar type")

    # Please use format 'mm-dd-yyyy'
    def set_date(self, date_str):
        month, day, year = date_str.split('-')
        time.sleep(1)
        self._select_year(year)
        self._select_month(month)
        self._select_day(day)

    # Protected method to select year
    def _select_year(self, year):
        self._step.click_on_element(self._year_dropdown_trigger)
        self._step.click_element_by_text(self._year_options, year, scrollIntoView=True, smartScroll=True)

    # Protected method to select month
    def _select_month(self, month):
        self._step.click_on_element(self._month_dropdown_trigger)
        month_text = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"][int(month)-1]
        self._step.click_element_by_text(self._month_options, month_text, scrollIntoView=True, smartScroll=True)

    # Protected method to select day
    def _select_day(self, day):
        if self._calendar_type == CalendarType.DEFAULT:
            day_locator = f'{self._parent_selector}//div[contains(@class, "picker__day") and text()="{int(day)}"]'
            self._step.click_on_element(day_locator)
        elif self._calendar_type == CalendarType.OXD:
            day_locator = f'//div[contains(@class, "oxd-calendar-date") and text()="{int(day)}"]'
            self._step.click_on_element(day_locator)