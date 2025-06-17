from selenium.webdriver.support import expected_conditions as EC
from data.data import TestData
from locators.locators import Locators
from selenium.webdriver.common.by import By #нужен будет для проверки цвета рамки неправильного пароля


class TestRegistration:
    def test_positive_registration_sucessfull(self, driver, wait):
        dfe = driver.find_element

        driver.get(TestData.BASE_URL)
        # клик "Вход и регистрация"
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_AND_REG_BTN))
        dfe(*Locators.LOGIN_AND_REG_BTN).click()
        wait.until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BTN)).click()

        # заполняем форму
        email = TestData.generate_email()
        password = TestData.generate_password()

        wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT)).send_keys(email)
        dfe(*Locators.PASSWORD_INPUT).send_keys(password)
        dfe(*Locators.REPEAT_INPUT).send_keys(password)
        dfe(*Locators.SUBMIT_BTN).click()

        # проверяем, что вошли
        assert wait.until(EC.visibility_of_element_located(Locators.AVATAR))
        assert dfe(*Locators.USERNAME).text == "User."


    def test_invalid_email_error(self, driver, wait):
        dfe = driver.find_element

        driver.get(TestData.BASE_URL)

        # Открываем форму логина
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_AND_REG_BTN))
        dfe(*Locators.LOGIN_AND_REG_BTN).click()
        # Открываем форму регистрации
        wait.until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BTN))
        dfe(*Locators.NO_ACCOUNT_BTN).click()
        # Вводим неправильный имейл
        dfe(*Locators.EMAIL_INPUT).send_keys(TestData.INVALID_EMAIL)
        dfe(*Locators.PASSWORD_INPUT).send_keys(TestData.EXISTING_PASSWORD)
        dfe(*Locators.REPEAT_INPUT).send_keys(TestData.EXISTING_PASSWORD)
        # Отправляем форму
        dfe(*Locators.SUBMIT_BTN).click()

        assert wait.until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MSG)).text == "Ошибка"

        #Проверка подстветки всех трех полей красным цветом
        for locator in [Locators.EMAIL_INPUT, Locators.PASSWORD_INPUT, Locators.REPEAT_INPUT]:
            input_element = driver.find_element(*locator)
            parent = input_element.find_element(By.XPATH, "./..")
            parent_class = parent.get_attribute("class")
            print(f"Checking {locator}: parent class = {parent_class}")
            assert "input_inputError__fLUP9" in parent_class


    def test_existed_user_registration_error(self, driver, wait):
        dfe = driver.find_element

        driver.get(TestData.BASE_URL)

        # Открываем форму логина
        wait.until(EC.element_to_be_clickable(Locators.LOGIN_AND_REG_BTN))
        dfe(*Locators.LOGIN_AND_REG_BTN).click()
        # Открываем форму регистрации
        wait.until(EC.element_to_be_clickable(Locators.NO_ACCOUNT_BTN))
        dfe(*Locators.NO_ACCOUNT_BTN).click()
        # Вводим существующий имейл
        dfe(*Locators.EMAIL_INPUT).send_keys(TestData.EXISTING_EMAIL)
        dfe(*Locators.PASSWORD_INPUT).send_keys(TestData.EXISTING_PASSWORD)
        dfe(*Locators.REPEAT_INPUT).send_keys(TestData.EXISTING_PASSWORD)
        # Отправляем форму
        dfe(*Locators.SUBMIT_BTN).click()

        assert wait.until(EC.visibility_of_element_located(Locators.EMAIL_ERROR_MSG)).text == "Ошибка"