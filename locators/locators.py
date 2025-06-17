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
    CREATE_AD_BTN     = (By.XPATH, "//button[text() = 'Разместить объявление']")
    LOGIN_MODAL_TITLE = (By.XPATH, "//div[contains(@class,'modal') or contains(@class,'popUp')]/h1")

    # Форма объявления
    TITLE_INPUT       = (By.NAME, "name")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description' and @placeholder='Описание товара']")
    PRICE_INPUT       = (By.NAME, "price")

    CATEGORY_DROPDOWN = ( By.XPATH, "//input[@name='category']/following-sibling::button" ) 
    CATEGORY_OPTION = (By.XPATH, "//span[text() = 'Книги']") 

    CITY_DROPDOWN_BTN = (By.XPATH, "//input[@name='city']/following-sibling::button")
    CITY_OPTION_SPB = (By.XPATH, "//span[text() = 'Санкт-Петербург']")

    CONDITION_USED = (By.XPATH, "//label[normalize-space()='Б/У']")

    PUBLISH_BTN = (By.CSS_SELECTOR, "button.buttonPrimary.inButtonText[type='submit']")  # Updated

    # Профиль
    AVATAR_BTN = (By.CSS_SELECTOR, "button.circleSmall:has(svg.svgSmall)")
    AVATAR_LINK = (By.XPATH, "//div[@class='App_app__GuJBs']" )
    MY_ADS_HEADER = (By.XPATH, "//h1[text()='Мои объявления']")
    AD_CARD       = (By.CSS_SELECTOR, "div.card")
    NEXT_PAGE_BTN = (By.XPATH, "//div[contains(@class,'pagination')]/button[last()]")
    PROFILE_AD_TITLE = staticmethod(lambda text: (By.XPATH, f"//div[contains(@class,'card')]//h2[normalize-space()='{text}']"))

    #Перехода по страницам объявления
    FIRST_ADD = (By.XPATH, "//div[@class = 'description']")
    PAGE_CURRENT = (By.CSS_SELECTOR, "div.card")
    PAGE_NEW = (By.CSS_SELECTOR, "div.card")
    


    