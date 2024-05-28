from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class FakeUser:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password_hash)

def get_hardcoded_user():
    return FakeUser(username="testuser", password="testpassword")
