import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By

driver = webdriver.Remote(
    command_executor=('http://selenium-env:4444/wd/hub'),
    desired_capabilities=DesiredCapabilities.FIREFOX)

def test_increment():
    driver.get("http://devops_flask_app:5555/")

    counter = driver.find_element(By.ID, "counter")
    counter = int(counter.text) + 1

    button = driver.find_element(By.ID, "plus")
    button.click()

    newcounter = driver.find_element(By.ID, "counter")
    newcounter = int(newcounter.text)

    assert counter == newcounter

    driver.close()


def test_decrement():
    driver.get("http://devops_flask_app:5555/")

    counter = driver.find_element(By.ID, "counter")
    counter = int(counter.text) - 1

    button = driver.find_element(By.ID, "minus")
    button.click()

    newcounter = driver.find_element(By.ID, "counter")
    newcounter = int(newcounter.text)

    assert counter == newcounter

    driver.close()