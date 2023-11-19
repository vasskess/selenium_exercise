import time

# Importing helper functions and constants
from booking.helpers.popup_remover import remove_popup_if_presented
from booking.helpers.click_helper import click_with_delay
import booking.constants as const

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Creating a Booking class that inherits from the Chrome WebDriver
class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        # Represents the ChromeOptions object, which allows customization of browser behavior.
        self.options = webdriver.ChromeOptions()
        #  Adds an experimental option to detach the browser window from the driver.
        self.options.add_experimental_option("detach", True)
        #  Represents the ChromeService object, which configures the ChromeDriver.
        self.service = ChromeService(ChromeDriverManager().install())
        # Boolean flag to determine whether to close the browser on exit
        self.teardown = teardown
        # Calling the constructor of the parent class
        super().__init__(service=self.service, options=self.options)
        """ Sets the implicit wait time to 5 seconds, allowing the WebDriver to wait
        for elements to be located before raising an exception."""
        self.implicitly_wait(5)
        #  Maximizes the browser window
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Closing the browser if the teardown flag is set
        if self.teardown:
            time.sleep(2)
            self.quit()

    def land_first_page(self):
        # Navigating to the base URL
        self.get(const.BASE_URL)

    def accept_cookies(self):
        # Locating and clicking the accept cookies button
        accept_btn = self.find_element(by=By.ID, value="onetrust-accept-btn-handler")
        click_with_delay(accept_btn)
        # Removing popup if presented
        remove_popup_if_presented(self)

    def change_language(self):
        # Locating and clicking the language button
        language_button = self.find_element(
            by=By.CSS_SELECTOR, value="[data-testid='header-language-picker-trigger']"
        )
        click_with_delay(language_button)

        # Locating and clicking the language selection button
        select_language = self.find_element(
            by=By.XPATH, value="//button[contains(., 'Български')]"
        )
        click_with_delay(select_language)
        # Removing popup if presented
        remove_popup_if_presented(self)

    def select_location(self):
        # Locating the input field and entering a location
        input_field = self.find_element(by=By.CSS_SELECTOR, value="[name='ss']")
        input_field.send_keys("Vratza")

    def select_dates(self):
        # Locating and clicking the date field
        date_field = self.find_element(
            by=By.CSS_SELECTOR, value="[data-testid='searchbox-dates-container']"
        )
        click_with_delay(date_field)

        # Locating and clicking the switch month button twice
        switch_month_button = self.find_element(
            by=By.XPATH,
            value="//div[@data-testid='searchbox-datepicker-calendar']/button",
        )
        click_with_delay(switch_month_button)
        click_with_delay(switch_month_button)

        # Locating and clicking the check-in and check-out dates
        check_in_date = self.find_element(
            by=By.CSS_SELECTOR, value="[data-date='2024-02-14']"
        )
        check_out_date = self.find_element(
            by=By.CSS_SELECTOR, value="[data-date='2024-02-16']"
        )
        click_with_delay(check_in_date)
        click_with_delay(check_out_date)

    def select_adults(self):
        # Locating and clicking the occupancy configuration field
        selection_field = self.find_element(
            by=By.CSS_SELECTOR, value="[data-testid='occupancy-config']"
        )
        selection_field.click()

        # Decreasing the number of adults to 1
        while True:
            decrease_adults_button = self.find_element(
                by=By.XPATH, value="//div[@class='bfb38641b0']/button"
            )
            click_with_delay(decrease_adults_button)

            adult_value_element = self.find_element(by=By.ID, value="group_adults")
            adult_value = adult_value_element.get_attribute("value")

            if int(adult_value) == 1:
                break

        # Increasing the number of adults and rooms based on predefined constants
        increase_adults_button = self.find_element(
            by=By.XPATH, value="//div[@class='bfb38641b0']/button[last()]"
        )
        # //div[@class='bfb38641b0']/button[2] - this is also usable for this case !

        for _ in range(const.ADULTS):
            click_with_delay(increase_adults_button)

        increase_rooms_button = self.find_element(
            by=By.XPATH,
            value="//div[@class='a7a72174b8'][last()]/div[@class='bfb38641b0']/button[last()]",
        )

        for _ in range(const.ROOMS):
            click_with_delay(increase_rooms_button)

    def perform_search(self):
        # Locating and clicking the search button
        search_button = self.find_element(
            by=By.CSS_SELECTOR, value="button[type='submit']"
        )
        click_with_delay(search_button)
