from selenium.webdriver.support import expected_conditions as EC
from data.data import TestData
from locators.locators import Locators


class TestLogout:
    def test_logout_shown_main_page(self, driver, wait):
        dfe = driver.find_element

        driver.get(TestData.BASE_URL)

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_AND_REG_BTN))
        dfe(*Locators.LOGIN_AND_REG_BTN).click()
        
        wait.until(EC.element_to_be_clickable(Locators.EXIST_EMAIL))

        dfe(*Locators.EXIST_EMAIL).send_keys(TestData.EXISTING_EMAIL)
        dfe(*Locators.EXIST_PASSORD).send_keys(TestData.EXISTING_PASSWORD)
        dfe(*Locators.LOGIN_BTN).click()
        
        wait.until(EC.element_to_be_clickable(Locators.LOG_OUT_BTN))
        dfe(*Locators.LOG_OUT_BTN).click()



        # проверяем, что вышли
        assert wait.until(EC.invisibility_of_element_located(Locators.AVATAR))
        assert wait.until(EC.visibility_of_element_located(Locators.LOGIN_AND_REG_BTN))
    