import random
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from data.data import TestData
from selenium.webdriver.common.by import By

class TestCreateListingAuth:
    def _login(self, driver, wait):
        dfe = driver.find_element

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_AND_REG_BTN))
        dfe(*Locators.LOGIN_AND_REG_BTN).click()

        wait.until(EC.visibility_of_element_located(Locators.EMAIL_INPUT))
        dfe(*Locators.EMAIL_INPUT).send_keys(TestData.EXISTING_EMAIL)

        wait.until(EC.visibility_of_element_located(Locators.PASSWORD_INPUT))
        dfe(*Locators.PASSWORD_INPUT).send_keys(TestData.EXISTING_PASSWORD)

        wait.until(EC.element_to_be_clickable(Locators.LOGIN_BTN))
        dfe(*Locators.LOGIN_BTN).click()

        wait.until(EC.visibility_of_element_located(Locators.AVATAR))

    def test_create_listing_auth_success(self, driver, wait):
        dfe = driver.find_element
        product=TestData.PRODUCT

        driver.get(TestData.BASE_URL)
        self._login(driver, wait)

        wait.until(EC.element_to_be_clickable(Locators.CREATE_AD_BTN))
        dfe(*Locators.CREATE_AD_BTN).click()
        
        wait.until(EC.visibility_of_element_located(Locators.TITLE_INPUT))
        dfe(*Locators.TITLE_INPUT).send_keys(product)


        wait.until(EC.visibility_of_element_located(Locators.DESCRIPTION_INPUT))
        dfe(*Locators.DESCRIPTION_INPUT).click()
        dfe(*Locators.DESCRIPTION_INPUT).send_keys("Описание")

        wait.until(EC.visibility_of_element_located(Locators.PRICE_INPUT))
        dfe(*Locators.PRICE_INPUT).send_keys("1000")

        # Категория
        wait.until(EC.element_to_be_clickable(Locators.CATEGORY_DROPDOWN))
        dfe(*Locators.CATEGORY_DROPDOWN).click()
        wait.until(EC.element_to_be_clickable(Locators.CATEGORY_OPTION))
        dfe(*Locators.CATEGORY_OPTION).click()

        # Город
        wait.until(EC.element_to_be_clickable(Locators.CITY_DROPDOWN_BTN))
        dfe(*Locators.CITY_DROPDOWN_BTN).click()

        
        wait.until(EC.element_to_be_clickable(Locators.CITY_OPTION_SPB))
        dfe(*Locators.CITY_OPTION_SPB).click()

        # Состояние Б/У
        wait.until(EC.element_to_be_clickable(Locators.CONDITION_USED))
        dfe(*Locators.CONDITION_USED).click()

        # Опубликовать
        wait.until(EC.element_to_be_clickable(Locators.PUBLISH_BTN))
        dfe(*Locators.PUBLISH_BTN).click()
        
        import time
        driver.execute_script("window.scrollTo(0, 0);")  # Scroll to top
        time.sleep(2)  #doesnt work without using sleep here
        wait.until(EC.element_to_be_clickable(Locators.AVATAR_BTN))
        dfe(*Locators.AVATAR_BTN).click()
        time.sleep(2)  
        wait.until(EC.visibility_of_element_located(Locators.MY_ADS_HEADER))

        title_xpath = (By.XPATH, f"//div[contains(@class, 'card')]//h2[normalize-space()='{product}']")
        driver.implicitly_wait(2)  # Short implicit wait for element lookup
        found = False
        for _ in range(30):  # максимум 30 кликов «дальше»
            print(f"Checking page {_ + 1}")  # Debug progress
            if driver.find_elements(*title_xpath):
                found = True
                break
            if driver.find_elements(*Locators.NEXT_PAGE_BTN):
                wait.until(EC.element_to_be_clickable(Locators.NEXT_PAGE_BTN))
                dfe(*Locators.NEXT_PAGE_BTN).click()
                wait.until(EC.staleness_of(driver.find_elements(By.CSS_SELECTOR, "div.card")[0]))  # Wait for old cards to go stale
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.card")))  # Wait for new cards
            else:
                break  # пагинация закончилась

        driver.implicitly_wait(5)  # Restore default implicit wait
        if not found:
            print("Page source:", driver.page_source[:1000])  # Debug page content
        assert found, f"Объявление «{product}» не найдено за 30 страниц"