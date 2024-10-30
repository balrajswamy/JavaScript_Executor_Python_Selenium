# conftest.py
import pytest
from selenium import webdriver
import logging
import os
import time


@pytest.fixture(scope="session")
def setup_browser():
    # Logging configuration


    try:
         # Creates the directory if it doesn’t exist
        logging.basicConfig(filename='LogsReports.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')


        logger = logging.getLogger()
        logger.info("Browser started the test session.")

        # Browser setup
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

        # Logging teardown
        logger.info("Browser closed after the test session.")
        logging.shutdown()
    except Exception as e1:
        print("Logs folder is missing!\t"+str(e1))



