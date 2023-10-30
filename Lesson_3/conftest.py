import pytest
from selenium import webdriver
import yaml

@pytest.fixture(scope="session")
def config():
    with open("testdata.yaml", encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config

@pytest.fixture(scope="function")
def browser(config):
    if config['browser'] == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise ValueError("This browser is not supported yet")
    driver.get(config['address'])
    yield driver
    driver.quit()
