def login(driver, credentials):
    email_input = driver.find_element_by_css_selector('input[name="email"]')
    pass_input = driver.find_element_by_css_selector('input[name="password"]')
    submit_button = driver.find_element_by_css_selector('input[type="submit"]')
    email_input.send_keys(credentials['email'])
    pass_input.send_keys(credentials['password'])
    submit_button.click()

    driver.find_element_by_xpath("//nav//*[contains(text(), 'Diet')]")
