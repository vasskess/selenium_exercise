# import time

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# accept_btn = driver.find_element(by=By.ID, value="onetrust-accept-btn-handler")
# time.sleep(2)
# accept_btn.click()
import booking.constants as const
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Booking(webdriver.Chrome):
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.service = ChromeService(ChromeDriverManager().install())
        super().__init__(service=self.service, options=self.options)

    def land_first_page(self):
        self.get(const.BASE_URL)
