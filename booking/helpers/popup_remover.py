from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from booking.helpers.click_helper import click_with_delay


def remove_popup_if_presenter(driver):
    try:
        # Try to locate the profile dialog element
        profile_dialog = driver.find_element(by=By.CLASS_NAME, value="eb33ef7c47")

        # Try to locate the close dialog window element with multiple aria-label values
        close_dialog_window = driver.find_element(
            by=By.CSS_SELECTOR,
            value="[aria-label='Затваряне на информацията за влизане в профила.'],"
            " [aria-label='Dismiss sign in information.'], [aria-label='Dismiss sign-in info.']",
        )

        # Click on the close dialog window element to remove the popup
        click_with_delay(close_dialog_window)

    except NoSuchElementException:
        # Handle the case when the popup is not presented
        print("Pop-up not presented!")
