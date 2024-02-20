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

    # Browse to the app
    driver.get("http://localhost:3000")  # TODO: Grab from workload var.args
    assert "React" in driver.title

    # Simulate button press
    reverse_button = driver.find_element(By.CLASS_NAME, "reverse")
    reverse_button.click()

    # Wait for a while to see the effect
    time.sleep(6)

    # Simulate button press
    filter_button = driver.find_element(By.CLASS_NAME, "filter-id")
    filter_button.click()

    # Wait for a while to see the effect
    time.sleep(6)

    # Simulate button press
    map_button = driver.find_element(By.CLASS_NAME, "map")
    map_button.click()

    # Wait for a while to see the effect
    time.sleep(5)

    # Close the browser window
    driver.quit()