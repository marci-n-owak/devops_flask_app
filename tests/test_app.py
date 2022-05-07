import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_increment():
    driver = webdriver.Chrome()
    driver.get("http://firefox-env:5555/")

    counter = driver.find_element(By.ID, "counter")
    counter = int(counter.text) + 1

    button = driver.find_element(By.ID, "plus")
    button.click()

    newcounter = driver.find_element(By.ID, "counter")
    newcounter = int(newcounter.text)

    assert counter == newcounter

    driver.close()


def test_decrement():
    driver = webdriver.Chrome()
    driver.get("http://firefox-env:5555/")

    counter = driver.find_element(By.ID, "counter")
    counter = int(counter.text) - 1

    button = driver.find_element(By.ID, "minus")
    button.click()

    newcounter = driver.find_element(By.ID, "counter")
    newcounter = int(newcounter.text)

    assert counter == newcounter

    driver.close()