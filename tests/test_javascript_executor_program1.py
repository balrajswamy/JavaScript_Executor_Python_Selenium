import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@allure.title("TestCase #1 to execute the JS Executor!")
@allure.description("Verifying the JS executor")
@allure.step("Checking Alerts is having OK button in popup")
def test_javascript():

    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    time.sleep(3)
    driver.maximize_window()

    with allure.step("Waiting for an alert!"):
        driver.execute_script("alert(1000)")

        time.sleep(3)

    driver.quit()
