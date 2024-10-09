from selenium.webdriver.common.by import By

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

class ReportsAnalytics:
    loading_spinner = '.oxd-loading-spinner'
    new_folder_button = 'button[tooltip="New Folder"]'
    folder_manipulation_message = '//div[@class="oxd-toast-content oxd-toast-content--success"]/p[2]'
    folder_names_list = '//div[@class="reports-accordion-header-title"]/p' # '.reports-accordion-header-title'
    folder_delete_confirmation_header = '//p[text()="Are you sure?"]'
    folder_delete_confirm = '//div[text()="Yes, Delete"]'


    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def wait_for_page_loading(self):
        self.step.specified_element_is_not_present(self.loading_spinner, 30)

    def click_on_new_folder_button(self):
        self.step.click_on_element(self.new_folder_button)

    def get_manipulation_meassage_text(self):
        self.step.wait_for_element(self.folder_manipulation_message)
        return self.step.get_element_text(self.folder_manipulation_message)

    def get_folder_names_list(self):
        return self.step.get_elements_texts(self.folder_names_list)

    def find_and_click_delete_button_for_folder(self, random_name):
        folder_elements = self.step.wd.find_elements(By.XPATH, self.folder_names_list)
        for folder_element in folder_elements:
            if folder_element.text == random_name:
                delete_button = folder_element.find_element(By.XPATH, './following::div//button[@tooltip="Delete"]')
                delete_button.click()

    def confirm_folder_deleting(self):
        self.step.wait_for_element(self.folder_delete_confirmation_header)
        self.step.click_on_element(self.folder_delete_confirm)