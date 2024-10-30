# js_executor.py
import logging

logger = logging.getLogger()

def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    logger.info("Scrolled to element: %s", element)

def highlight_element(driver, element):
    driver.execute_script("arguments[0].style.border='3px solid red'", element)
    logger.info("Highlighted element: %s", element)

def get_element_text(driver, element):
    text = driver.execute_script("return arguments[0].textContent;", element)
    logger.info("Text from element: %s", text)
    return text
