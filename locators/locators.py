from selenium.webdriver.common.by import By

class Locators:

    #Страница перед входом
    LOGIN_AND_REG_BTN = (By.XPATH, ".//button[text() = 'Вход и регистрация']") # Вход и регистрация

    #Создать нового юзера
    NO_ACCOUNT_BTN = (By.XPATH, ".//button[text() = 'Нет аккаунта']") # Нет Аккаунта
    EMAIL_INPUT = (By.NAME, "email") # Введите имейл
    PASSWORD_INPUT = (By.NAME, "password") # Пароль
    REPEAT_INPUT = (By.NAME, "submitPassword") #Повторите пароль
    SUBMIT_BTN = (By.XPATH, ".//button[text() = 'Создать аккаунт']") #Создать аккаунт
    EMAIL_ERROR_MSG = (By.CSS_SELECTOR, ".input_span__yWPqB")  #Ошибка при вводе неправильного имейла

    #Для логина
    EXIST_EMAIL = (By.NAME, "email")
    EXIST_PASSORD = (By.NAME, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button.buttonPrimary.inButtonText[type='submit']")

    
    #Главная страница после логина
    AVATAR = (By.CSS_SELECTOR, ".svgSmall") #Иконка аватара
    USERNAME = (By.CSS_SELECTOR, ".profileText.name")  # Имя пользователя

    #Логин
    LOG_OUT_BTN = (By.CSS_SELECTOR, "button.spanGlobal.btnSmall")   

    #Разместить объявления
    CREATE_AD_BTN     = (By.XPATH, "/html/body/div/div/div[1]/div/button")
    LOGIN_MODAL_TITLE = (By.XPATH, "//div[contains(@class,'modal') or contains(@class,'popUp')]/h1")

    # Форма объявления
    TITLE_INPUT       = (By.NAME, "name")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description' and @placeholder='Описание товара']")
    PRICE_INPUT       = (By.NAME, "price")

    CATEGORY_DROPDOWN = ( By.XPATH, "//input[@name='category']/following-sibling::button" ) 
    CATEGORY_OPTION = (By.XPATH, ".//div/div/div[2]/div/form/div[2]/div[2]/div[2]/button[2]") 

    CITY_DROPDOWN_BTN = (By.XPATH, "//input[@name='city']/following-sibling::button")
    CITY_OPTION_SPB = (By.XPATH, "/html/body/div/div/div[2]/div/form/div[3]/div[2]/button[2]")

    CONDITION_USED = (By.XPATH, "//label[normalize-space()='Б/У']")

    PUBLISH_BTN = (By.CSS_SELECTOR, "button.buttonPrimary.inButtonText[type='submit']")  # Updated

    # Профиль
    AVATAR_BTN = (By.CSS_SELECTOR, "button.circleSmall:has(svg.svgSmall)")
    MY_ADS_HEADER = (By.XPATH, "//h1[text()='Мои объявления']")
    AD_CARD       = (By.CSS_SELECTOR, "div.card")
    NEXT_PAGE_BTN = (By.XPATH, "//div[contains(@class,'pagination')]/button[last()]")

    @staticmethod
    def PROFILE_AD_TITLE(text):
        return (By.XPATH, f"//*[self::h2 or self::h3 or self::div][normalize-space()='{text}']")
    



    