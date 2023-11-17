import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), options=options
)

driver.get("https://www.desmos.com/scientific/")

switch_mode = driver.find_element(
    by=By.CSS_SELECTOR, value=".dcg-keypad-control-btn[aria-label='settings']"
)
value_1 = driver.find_element(
    by=By.CSS_SELECTOR, value=".dcg-keypad-btn.dcg-btn-dark-on-gray[dcg-command='7']"
)
plus_btn = driver.find_element(
    by=By.CSS_SELECTOR, value=".dcg-keypad-btn.dcg-btn-light-on-gray[dcg-command='+']"
)
value_2 = driver.find_element(
    by=By.CSS_SELECTOR, value=".dcg-keypad-btn.dcg-btn-dark-on-gray[dcg-command='8']"
)
result = driver.find_element(
    by=By.CSS_SELECTOR, value=".dcg-keypad-btn.dcg-btn-short-blue[dcg-command='enter']"
)
time.sleep(2)
switch_mode.click()
time.sleep(2)
dark_mode = WebDriverWait(driver, 5).until(
    ec.presence_of_element_located(
        (
            By.CSS_SELECTOR,
            ".dcg-component-checkbox.dcg-settings-menu-option.dcg-do-not-blur.dcg-reverse-contrast",
        )
    )
)
dark_mode.click()
time.sleep(2)
value_1.click()
time.sleep(2)
plus_btn.click()
time.sleep(2)
value_2.click()
time.sleep(2)
result.click()
time.sleep(2)
driver.close()
