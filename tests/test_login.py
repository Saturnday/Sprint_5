from selenium.webdriver.support import expected_conditions as EC
from data.data import TestData
from locators.locators import Locators


class TestLogin:
    def test_login_main_page_shown_user_name(self, driver, wait):
        dfe = driver.find_element

        driver.get(TestData.BASE_URL)

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_AND_REG_BTN))
        dfe(*Locators.LOGIN_AND_REG_BTN).click()
        
        wait.until(EC.element_to_be_clickable(Locators.EXIST_EMAIL))

        dfe(*Locators.EXIST_EMAIL).send_keys(TestData.EXISTING_EMAIL)
        dfe(*Locators.EXIST_PASSORD).send_keys(TestData.EXISTING_PASSWORD)
        dfe(*Locators.LOGIN_BTN).click()

        # проверяем, что вошли
        assert wait.until(EC.visibility_of_element_located(Locators.AVATAR_BTN))
        assert wait.until(EC.visibility_of_element_located(Locators.LOGIN_AND_REG_BTN))
    