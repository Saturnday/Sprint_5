from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from data.data import TestData


class TestCreateListing:
    
    def test_create_listing_unauth_modal(self, driver, wait):
        driver.get(TestData.BASE_URL)

        wait.until(EC.element_to_be_clickable(Locators.CREATE_AD_BTN)).click()

        modal_title = wait.until(
            EC.visibility_of_element_located(Locators.LOGIN_MODAL_TITLE)
        ).text

        assert modal_title == "Войти"  