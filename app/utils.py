from passlib.context import CryptContext


class PasswordHelper:
    def __init__(self):
        self.context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, raw_password: str, hash_password: str) -> bool:
        return self.context.verify(raw_password, hash_password)

    def get_hash_password(self, raw_password: str) -> str:
        return self.context.hash(raw_password)


password_helper = PasswordHelper()
