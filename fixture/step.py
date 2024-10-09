import time

from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class StepHelper:

    def __init__(self, app):
        # Initializes an instance of the StepHelper class with the application context.
        self.app = app
        self.wd = self.app.wd

    def get_how(self, locator):
        # Determines how to locate an element based on the given locator string.
        if locator.startswith("//") or locator.startswith("(//"):
            how = By.XPATH
        else:
            how = By.CSS_SELECTOR
        return how

    def specified_element_is_present(self, locator, time=3):
        # Checks if a specified element is present on the page within a given timeframe.
        try:
            WebDriverWait(self.wd, time).until(
                EC.presence_of_element_located((self.get_how(locator), locator)))
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True

    def wait_for_element(self, locator, wait_time=10):
        # Waits for a specified element to be visible.
        element = WebDriverWait(self.wd, wait_time).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        return element

    def specified_element_is_not_present(self, locator, waitingTime=3):
        # Waits to ensure a specified element is not present or becomes invisible.
        time.sleep(1)
        WebDriverWait(self.wd, waitingTime).until(
            EC.invisibility_of_element_located((self.get_how(locator), locator)))

    def click_on_element(self, locator, pause_before_click=0.5, scrollInToView=False):
        # Clicks on a specified element, optionally scrolling into view and pausing before clicking.
        WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        element = WebDriverWait(self.wd, 10).until(
            EC.element_to_be_clickable((self.get_how(locator), locator))
        )
        if scrollInToView:
            self.wd.execute_script(
                "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });", element)
            time.sleep(2)
        ActionChains(self.wd).move_to_element(element).pause(pause_before_click).click().perform()

    def input_text(self, locator, text):
        # Enters text into a specified input field.
        element = WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        element.click()
        element.clear()
        element.send_keys(text)

    def get_list_of_elements(self, locator):
        # Returns a list of elements matching the specified locator.
        by = self.get_how(locator)
        WebDriverWait(self.wd, 10).until(
            EC.presence_of_all_elements_located((self.get_how(locator), locator)))
        return self.wd.find_elements(by=by, value=locator)

    def get_element_text(self, locator, scrollInToView=False):
        # Retrieves the text from a specified element, optionally scrolling it into view.
        element = WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        if scrollInToView:
            self.wd.execute_script(
                "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });", element)
            time.sleep(2)
        return element.text

    def get_element_attribute_value(self, locator, attribute, scrollInToView=False):
        # Retrieves the value of a specified attribute from an element, optionally scrolling it into view.
        element = WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        if scrollInToView:
            self.wd.execute_script(
                "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });", element)
            time.sleep(2)
        return element.get_attribute(attribute)

    def jsXpathClick(self, locator):
        # Performs a click on an element using JavaScript, specifically for XPATH locators.
        time.sleep(2)
        b = self.wd.find_element(By.XPATH, locator)
        self.wd.execute_script("arguments[0].click();", b)

    def select_dropdown_by_value(self, locator, value):
        # Selects an option from a dropdown element by its value.
        dropdown = WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        Select(dropdown).select_by_value(value)

    def select_dropdown_by_text(self, locator, text):
        # Selects an option from a dropdown element by the visible text.
        dropdown = WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        Select(dropdown).select_by_visible_text(text)

    def get_elements_texts(self, locator):
        # Retrieves texts from all elements matching the specified locator and returns them as a list.
        WebDriverWait(self.wd, 10).until(
            EC.presence_of_all_elements_located((self.get_how(locator), locator)))
        elements = self.wd.find_elements(self.get_how(locator), locator)
        texts = []
        for element in elements:
            self.wd.execute_script(
                "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });", element)
            text = element.get_attribute("textContent").strip()
            texts.append(text)
        return texts

    def click_element_by_text(self, locator, text, scrollIntoView=False, smartScroll=False):
        elements = self.get_list_of_elements(locator)
        for element in elements:
            if smartScroll:
                # Smart scrolling: scroll a little, then check if the element is visible
                self.wd.execute_script("arguments[0].scrollIntoView({block: 'nearest'});", element)
                time.sleep(0.5)
            if element.text == text and element.is_displayed():
                if scrollIntoView:
                    self.wd.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                           element)
                    time.sleep(1)
                element.click()
                break

    def click_element_containing_text(self, locator, text):
        """Clicks on an element containing the specified text, case-insensitively."""
        elements = self.get_list_of_elements(locator)
        text_lower = text.lower()  # Convert the search text to lowercase for case-insensitive comparison
        clicked = False

        for element in elements:
            element_text = element.text.lower()  # Convert each element's text to lowercase
            if text_lower in element_text:
                print(f"\nAttempting to click on element containing text: '{text}' with actual text: '{element.text}'")
                try:
                    element.click()
                    clicked = True
                    print("\nClick successful.")
                    break  # Exit the loop after clicking
                except Exception as e:
                    print(f"Failed to click on the element. Error: {e}")

        if not clicked:
            print(f"No clickable element found containing text: '{text}'")

    def scroll_element_into_center(self, locator):
        element = WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        self.wd.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)

    def assert_lists_equal_with_diff(self, actual, expected):
        try:
            # Utilize assert_that from the Application class
            self.app.assert_that(sorted(actual)).is_equal_to(sorted(expected))
        except AssertionError as e:
            # Calculate differences
            actual_set = set(actual)
            expected_set = set(expected)
            expected_but_missing = expected_set - actual_set
            found_but_not_expected = actual_set - expected_set
            # Constructing the detailed error message
            error_message = (
                f"{str(e)}\n"
                f"Items expected to be in the list but missing: {expected_but_missing}\n"
                f"Items not expected to be in the list but found: {found_but_not_expected}"
            )
            raise AssertionError(error_message) from None

    def switch_to_tab_by_title(self, partial_title):
        # Switches to a tab where the title contains the given substring.
        current_window = self.wd.current_window_handle
        for handle in self.wd.window_handles:
            self.wd.switch_to.window(handle)
            if partial_title in self.wd.title:
                return True
        # Switch back to the original window if no matching title is found
        self.wd.switch_to.window(current_window)
        return False

    def switch_to_tab_by_url(self, full_url):
        current_window = self.wd.current_window_handle
        for handle in self.wd.window_handles:
            self.wd.switch_to.window(handle)
            if self.wd.current_url == full_url:
                return
        self.wd.switch_to.window(current_window)

    def switch_to_iframe(self, locator):
        iframe_element = self.wait_for_element(locator)
        self.wd.switch_to.frame(iframe_element)

    def switch_to_default_content(self):
        self.wd.switch_to.default_content()