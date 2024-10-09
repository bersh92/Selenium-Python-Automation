from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver


class SideMenu:
    side_menu_one = 'div[class="sidebar menu-visible"][class="sidebar menu-visible"]:not([ng-class]) li[id*="left_menu_item"]'
    side_menu_two = 'div[id="menu-container"]  li[class="menu-level-2"] a:nth-child(1) span'
    more_button = "//span[text()='More']"

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def click_on_side_menu_button(self, element_text):
        try:
            self.step.click_element_by_text(self.side_menu_two, element_text, True, True)
        except:
            self.step.click_element_by_text(self.side_menu_one, element_text, True, True)