from selenium.webdriver.support import expected_conditions as EC
from locators.locators import Locators
from data.data import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class TestCreateListingAuth:

    def test_create_listing_auth_success(self, driver, wait, login):
        dfe = driver.find_element
        product=TestData.PRODUCT
        driver.get(TestData.BASE_URL)

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

        wait.until(EC.element_to_be_clickable(Locators.AVATAR))
        driver.get(TestData.MY_PROFILE)
        wait.until(EC.visibility_of_element_located(Locators.MY_ADS_HEADER))
    

        title_xpath = (By.XPATH, f"//div[contains(@class, 'card')]//h2[normalize-space()='{product}']")
        driver.implicitly_wait(2)  # Short implicit wait for element lookup

        
        found = False
        for _ in range(30):
            if driver.find_elements(*title_xpath):
                found = True
                break
            if driver.find_elements(*Locators.NEXT_PAGE_BTN):
                # запоминаем старые карточки, чтобы отследить их «устаревание»      # FIX
                old_cards = driver.find_elements(*Locators.AD_CARD)                 # FIX
                wait.until(EC.element_to_be_clickable(Locators.NEXT_PAGE_BTN)).click()
                if old_cards:                                                       # FIX
                    wait.until(EC.staleness_of(old_cards[0]))                       # FIX
                wait.until(EC.presence_of_element_located(Locators.AD_CARD))        # FIX
            else:
                break

        assert found, f"Объявление «{product}» не найдено за 30 страниц"