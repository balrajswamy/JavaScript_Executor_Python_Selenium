# conftest.py
import pytest
from selenium import webdriver
import logging
import os


@pytest.fixture(scope="session")
def setup_browser():
    # Define the directory and file path for the log file
    logfile_path = "C:\\AutomationTestingCourse\\Python_Selenium_Projects\\Logs\\"
    log_file = logfile_path + "LogsReports.log"

    # Create the directory if it doesn’t exist
    if not os.path.exists(logfile_path):
        os.makedirs(logfile_path)

    # Logging configuration
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    logger = logging.getLogger()
    logger.info("Browser started the test session.")

    # Browser setup
    try:
        driver = webdriver.Chrome()
        driver.maximize_window()
        yield driver
        driver.quit()

        # Logging teardown
        logger.info("Browser closed after the test session.")
    except Exception as e1:
        logger.error(f"An error occurred during browser setup or teardown: {str(e1)}")
        print("Logs folder is missing!\t" + str(e1))
    finally:
        logging.shutdown()
