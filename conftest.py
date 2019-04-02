import pytest
import uuid

from selenium.webdriver.firefox.options import Options
from selenium import webdriver

options = Options()
options.headless = False

@pytest.fixture
def driver():
    d = webdriver.Firefox(options=options, executable_path='./geckodriver/geckodriver')
    d.implicitly_wait(10)
    yield d
    #d.quit()

@pytest.fixture
def root_url():
    return 'http://logs.hhixl.net:3000'

@pytest.fixture
def new_credentials():
    return {
        'email': 'testuser-%s@email.com'%uuid.uuid1(),
        'password': str(uuid.uuid1())
    }

@pytest.fixture
def existing_credentials():
    return {
        'email': 'asdf',
        'password': 'asdf'
    }
