from jose import jwt

from app.config import settings


class TokenHelper:
    PRIVATE_SECRET_KEY: str = settings.PRIVATE_SECRET_KEY
    ALGORITHM: str = "HS256"

    def get_token_payload(self, token: str):
        payload = jwt.decode(token, self.PRIVATE_SECRET_KEY, algorithms=[self.ALGORITHM])
        return payload


token_helper = TokenHelper()
