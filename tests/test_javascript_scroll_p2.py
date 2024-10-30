import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from js_executor import scroll_to_element, highlight_element, get_element_text


@allure.title("TestCase #1 to execute the JS Executor!")
@allure.description("Verifying the JS executor")
@allure.step("Checking Alerts is having OK button in popup")
def test_javascript():

    driver = webdriver.Chrome()
    driver.get("https://selectorshub.com/xpath-practice-page/")
    time.sleep(3)
    driver.maximize_window()
    time.sleep(3)

    with allure.step("Scrolling the web page!"):
        driver.execute_script("window.scrollBy(0,500);")
        driver.execute_script("window.scrollBy(0,500);")
        driver.execute_script("window.scrollBy(0,500);")
        driver.execute_script("window.scrollBy(0,500);")
        driver.execute_script("window.scrollBy(0,500);")

    time.sleep(10)
    driver.quit()
