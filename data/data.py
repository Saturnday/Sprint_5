import random

class TestData:
    BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"
    MY_PROFILE = "https://qa-desk.stand.praktikum-services.ru/profile"
    EXISTING_EMAIL = 'test_20_2025@yandex.com'
    EXISTING_PASSWORD = '123456'
    INVALID_EMAIL = "wrong-email"
    PRODUCT = f"Тестовый товар {random.randint(1000, 100000)}"
