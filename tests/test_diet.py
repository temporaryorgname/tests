import urllib

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from tests import utils

def test_create_delete_entry(driver, root_url, existing_credentials):
    driver.get(root_url)
    utils.login(driver, existing_credentials)

    diet_nav_button = driver.find_element_by_xpath('//nav//a//*[contains(text(), "Diet")]')
    diet_nav_button.click()

    driver.find_element_by_xpath('//*[contains(text(), "Diet Log")]')

    item_name_field = driver.find_element_by_name("item")
    item_name_field.click()
    item_name_field.clear()
    item_name_field.send_keys("thing")
    assert item_name_field.get_attribute('value') == 'thing'

    driver.find_element_by_name("quantity").clear()
    driver.find_element_by_name("quantity").send_keys("1")
    driver.find_element_by_name("calories").clear()
    driver.find_element_by_name("calories").send_keys("2")
    driver.find_element_by_name("protein").clear()
    driver.find_element_by_name("protein").send_keys("3")
    driver.find_element_by_name("protein").send_keys(Keys.ENTER)
    WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@name="item" and @value=""]'))
    )
    assert item_name_field.get_attribute('value') == ''

    # Check that the entry was created
    driver.find_element_by_xpath('//td//input[@value="thing"]')

    # Delete entry
    checkboxes = driver.find_elements_by_xpath('//td//input[@type="checkbox"]/ancestor::label')
    for cb in checkboxes:
        cb.click()
    delete_button = driver.find_element_by_xpath('//i[text()="delete"]/ancestor::a')
    delete_button.click()
    driver.switch_to.alert.accept()
    
    # Check if any entries still exist
    checkboxes = driver.find_elements_by_xpath('//td//input[@type="checkbox"]')
    assert len(checkboxes) == 0

    # Refresh and check that it's cleaned up
    driver.navigate().refresh()

    checkboxes = driver.find_elements_by_xpath('//td//input[@type="checkbox"]')
    assert len(checkboxes) == 0
