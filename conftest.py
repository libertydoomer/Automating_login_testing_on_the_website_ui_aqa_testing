import pytest
from selenium import webdriver
from pages.user_login import UserLogin
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    chrome_driver = webdriver.Chrome(options=options)
    return chrome_driver

@pytest.fixture()
def login_page(driver):
    return UserLogin(driver)