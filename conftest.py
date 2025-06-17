import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from data.data import TestData

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

@pytest.fixture
def login(driver, wait):
    driver.get(TestData.BASE_URL)
    wait.until(EC.element_to_be_clickable(Locators.LOGIN_AND_REG_BTN)).click()
    wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys(TestData.EXISTING_EMAIL)
    wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT)).send_keys(TestData.EXISTING_PASSWORD)
    wait.until(EC.element_to_be_clickable(Locators.LOGIN_BTN)).click()
    wait.until(EC.visibility_of_element_located(Locators.AVATAR_BTN))