from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IMDbSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.imdb.com/search/name/"

        # Locators for the input fields, select boxes, and buttons
        self.name_input_locator = (By.ID, 'name')  # Update this ID based on actual element
        self.gender_select_locator = (By.ID, 'gender')  # Update this ID based on actual element
        self.birth_date_input_locator = (By.ID, 'birth_date')  # Update this ID based on actual element
        self.search_button_locator = (By.XPATH, "//button[@type='submit']")  # Update this XPath based on actual element

    def load(self):
        """Navigate to the IMDb search page."""
        self.driver.get(self.url)

    def enter_name(self, name):
        """Enter the name into the input box."""
        name_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.name_input_locator)
        )
        name_input.clear()
        name_input.send_keys(name)

    def select_gender(self, gender):
        """Select a gender from the dropdown."""
        gender_select = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.gender_select_locator)
        )
        gender_select.click()
        gender_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f"//option[@value='{gender}']"))
        )
        gender_option.click()

    def enter_birth_date(self, birth_date):
        """Enter birth date into the input box."""
        birth_date_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.birth_date_input_locator)
        )
        birth_date_input.clear()
        birth_date_input.send_keys(birth_date)

    def click_search(self):
        """Click the search button."""
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_button_locator)
        )
        search_button.click()
