from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoAlertPresentException
import logging

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = "https://test-stand.gb.ru/"
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator))
            logging.debug(f"Element {locator} found")
            return element
        except TimeoutException:
            logging.error(f"Timeout error: element {locator} not found during {time} seconds")
        except NoSuchElementException:
            logging.error(f"Element {locator} not found")
        return None

    def find_elements(self, locator, time=10):
        try:
            elements = WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator))
            logging.debug(f"Elements {locator} found")
            return elements
        except TimeoutException:
            logging.error(f"Timeout error: elements {locator} not found during {time} seconds")
        except NoSuchElementException:
            logging.error(f"Elements {locator} not found")
        return []

    def go_to_site(self):
        try:
            self.browser.get(self.base_url)
            logging.info(f"Opened site {self.base_url}")
        except Exception as e:
            logging.error(f"An error occurred while trying to open site {self.base_url}: {e}")

    def get_alert_text(self):
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            logging.info("Alert found, text retrieved")
            return alert_text
        except NoAlertPresentException:
            logging.error("No alert present")
            return None
