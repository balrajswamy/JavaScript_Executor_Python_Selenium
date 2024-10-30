# test_javascript_executor.py
import time

import pytest
import allure
import logging
from selenium.webdriver.common.by import By
from .js_executor import scroll_to_element, highlight_element, get_element_text


logger = logging.getLogger()

@allure.feature("JavaScript Executor")
@allure.story("Execute JS actions in Selenium")
@pytest.mark.usefixtures("setup_browser")
class TestJSExecutor:

    @allure.step("Scroll to and highlight element, then retrieve text")
    def test_scroll_highlight_and_retrieve_text(self, setup_browser):
        driver = setup_browser
        driver.get("https://selectorshub.com/xpath-practice-page/")

        # Find element to interact with
        element = driver.find_element(By.XPATH, "//a[contains(text(),'SelectorsHub Youtube Channel')]")

        # Execute JS actions
        scroll_to_element(driver, element)
        highlight_element(driver, element)
        time.sleep(6)
        text = get_element_text(driver, element)

        # Logging the retrieved text

        logger.info("Retrieved text: %s", text)

        # Allure assertion with the retrieved text
        with allure.step("Validate retrieved text"):
            assert "SelectorsHub Youtube Channel" in text, "Text does not match expected value"
