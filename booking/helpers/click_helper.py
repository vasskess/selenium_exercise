import time


def click_with_delay(element, delay=2):
    time.sleep(delay)
    element.click()
