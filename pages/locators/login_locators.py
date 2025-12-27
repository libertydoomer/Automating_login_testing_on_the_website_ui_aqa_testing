from selenium.webdriver.common.by import By


username_field_loc = (By.ID, "user-name")
password_field_loc = (By.ID, "password")
button_loc = (By.ID, "login-button")
products_title_loc = (By.CSS_SELECTOR, '[data-test="title"]')
error_alert_loc = (By.CSS_SELECTOR, '[data-test="error"]')