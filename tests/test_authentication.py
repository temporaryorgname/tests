import urllib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests import utils

def test_signup(driver, root_url, new_credentials):
    driver.get(urllib.parse.urljoin(root_url,'signup'))
    name_input = driver.find_element_by_css_selector('input[name="name"]')
    email_input = driver.find_element_by_css_selector('input[name="email"]')
    pass1_input = driver.find_element_by_css_selector('input[name="password"]')
    pass2_input = driver.find_element_by_css_selector('input[name="password2"]')
    submit_button = driver.find_element_by_css_selector('input[type="submit"]')
    name_input.send_keys('Some user')
    email_input.send_keys(new_credentials['email'])
    pass1_input.send_keys(new_credentials['password'])
    pass2_input.send_keys(new_credentials['password'])
    submit_button.click()

    driver.find_element_by_xpath("//nav//*[contains(text(), 'Diet')]")

def test_login_logout(driver, root_url, existing_credentials):
    driver.get(root_url)
    utils.login(driver, existing_credentials)

    logout_button = driver.find_element_by_xpath('//nav//a//*[contains(text(), "Logout")]')
    logout_button.click()

    email_input = driver.find_element_by_css_selector('input[name="email"]')
