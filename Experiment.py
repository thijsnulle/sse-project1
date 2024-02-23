import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def run_tasks(settings):
    # Set Selenium webdriver
    driver = None
    if settings.name == "chrome":
        driver = webdriver.Chrome(r".\chromedriver-win64\chromedriver.exe")
    elif settings.name == "firefox":
        driver = webdriver.Firefox()  # TODO: PATH/TO/DRIVER
    elif settings.name == "safari":
        driver = webdriver.Safari()  # TODO: PATH/TO/DRIVER

    print("WEBDRIVER CHOSEN")

    # Browse to the app
    driver.get(f"{settings.ip}")
    driver.implicitly_wait(3)
    assert "React" in driver.title


    # Simulate button press
    reverse_button = driver.find_element(By.CLASS_NAME, "reverse")
    reverse_button.click()
    print("clicked reverse")

    # Wait for a while to see the effect
    time.sleep(1)

    # Simulate button press
    filter_button = driver.find_element(By.CLASS_NAME, "filter-id")
    filter_button.click()
    print("clicked filter")

    # Wait for a while to see the effect
    time.sleep(1)

    # Simulate button press
    map_button = driver.find_element(By.CLASS_NAME, "map")
    map_button.click()
    print("clicked map")

    # Wait for a while to see the effect
    time.sleep(1)

    # Close the browser window
    driver.quit()
    print("driver.quit()")
