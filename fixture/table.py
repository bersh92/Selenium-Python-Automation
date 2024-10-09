from typing import List, Dict

from selenium.webdriver.remote.webelement import WebElement

from fixture.step import StepHelper

class Table:
    def __init__(self, step: StepHelper, row_selector: str, column_selectors: Dict[str, str]):
        self.step = step
        self.row_selector = row_selector
        self.column_selectors = column_selectors

    class Row:
        def __init__(self, row_element: WebElement, column_selectors: Dict[str, str], step: StepHelper):
            self.row_element = row_element
            self.column_selectors = column_selectors
            self.step = step

        def __getitem__(self, column_name: str) -> str:
            selector = self.column_selectors.get(column_name)
            if selector:
                # Use the step method to get element text, considering selector type
                element = self.row_element.find_element(self.step.get_how(selector), selector)
                return element.text
            raise ValueError(f"No selector available for column: {column_name}")

        def click_column_button(self, column_name: str):
            """Clicks a button or checkbox located in the specified column of this row."""
            selector = self.column_selectors.get(column_name)
            if selector:
                # Use the step method to perform click, considering selector type
                self.row_element.find_element(self.step.get_how(selector), selector).click()
            else:
                raise ValueError(f"No selector available for column: {column_name}")

    def get_rows(self) -> List['Row']:
        # Use the step method to locate row elements, considering selector type
        row_elements = self.step.get_list_of_elements(self.row_selector)
        return [Table.Row(element, self.column_selectors, self.step) for element in row_elements]

    def __getitem__(self, index: int) -> 'Row':
        rows = self.get_rows()
        if index < len(rows):
            return rows[index]
        raise IndexError("Row index out of range")

    def get_column_data(self, column_name: str) -> List[str]:
        rows = self.get_rows()
        return [row[column_name] for row in rows]

    def click_all_in_column(self, column_name: str):
        """Clicks all buttons or checkboxes in the specified column."""
        rows = self.get_rows()
        for row in rows:
            row.click_column_button(column_name)
