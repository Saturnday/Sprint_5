import random
import string

class TestData:
    BASE_URL = "https://qa-desk.stand.praktikum-services.ru/"
    EXISTING_EMAIL = 'test_20_2025@yandex.com'
    EXISTING_PASSWORD = '123456'
    INVALID_EMAIL = "wrong-email"
    PRODUCT = f"Тестовый товар {random.randint(1000, 100000)}"

#Random email for testing registration:
    @staticmethod
    def _rand_str(k: int = 10) -> str:
        alphabet = string.ascii_letters + string.digits
        return "".join(random.choices(alphabet, k=k))

    @classmethod
    def generate_email(cls) -> str:
        return f"{cls._rand_str()}@test.com"

    @classmethod
    def generate_password(cls) -> str:
        return cls._rand_str()
