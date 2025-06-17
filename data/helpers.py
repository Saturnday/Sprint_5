import random
import string
from selenium.webdriver.common.by import By

class TestHelpers:

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
    
    @staticmethod
    def PROFILE_AD_TITLE(text):
        return (By.XPATH, f"//*[self::h2 or self::h3 or self::div][normalize-space()='{text}']") 
