import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import IMDbSearchPage
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    # Initialize the WebDriver
    driver = webdriver.Chrome()  # Ensure ChromeDriver is correctly installed and in PATH
    yield driver
    driver.quit()

def test_imdb_search(driver):
    # Initialize IMDb search page object
    search_page = IMDbSearchPage(driver)

    # Load the IMDb search page
    search_page.load()

    # Enter data into the form fields
    search_page.enter_name('Vijay')
    search_page.select_gender('male')
    search_page.enter_birth_date('1993')

    # Click the search button
    search_page.click_search()

    # Verify that results are displayed on the page
    assert WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'lister-item-header'))
    )
