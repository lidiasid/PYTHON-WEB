from testpage import OperationsHelper
import logging
import yaml

with open("testdata.yaml", encoding='utf-8') as f:
    testdata = yaml.safe_load(f)

def test_step1(browser):
    logging.info("Test1 Starting")
    testpage = OperationsHelper(browser)
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"

def test_step2(browser, config):
    logging.info("Test2 Starting")
    testpage = OperationsHelper(browser)
    testpage.enter_login(config.get("login"))
    testpage.enter_pass(config.get("passwd"))
    testpage.click_login_button()
    assert "hello" in testpage.get_text().lower(), "Test FAILED"

def test_step3(browser, config):
    logging.info("Test3 Starting")
    testpage = OperationsHelper(browser)
    testpage.enter_login(config.get("login"))
    testpage.enter_pass(config.get("passwd"))
    testpage.click_login_button()
    testpage.click_contact_button()
    testpage.enter_name(config.get("name"))
    testpage.enter_email(config.get("email"))
    testpage.enter_content(config.get("content"))
    testpage.click_contact_us_button()
    assert testpage.get_alert_message() == "Form successfully submitted", "Test FAILED"