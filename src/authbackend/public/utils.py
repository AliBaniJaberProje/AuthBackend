from datetime import datetime, timedelta
import bcrypt
import jwt
from typing import Optional

from authbackend.constants import SECRET_KEY, REFRESH_SECRET_KEY, REFRESH_TOKEN_EXPIRE_DAYS, ACCESS_TOKEN_EXPIRE_MINUTES

from src.authbackend.exceptions import ExpiredTokenError


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))

def create_access_token(user_id: int, social_login: bool, email: str) -> str:
    payload = {"user_id": user_id, "social_login":social_login, "email":email, "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def create_refresh_token(user_id: int, social_login: bool, email: str) -> str:
    payload = {"user_id": user_id, "social_login":social_login, "email":email, "exp": datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)}
    return jwt.encode(payload, REFRESH_SECRET_KEY, algorithm="HS256")

def decode_access_token(token: str) -> Optional[dict]:
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        print("Expired token")
        raise ExpiredTokenError("expired token")
    except jwt.InvalidTokenError:
        print("Invalid token")
        raise InvalidTokenError("Invalid token")

def decode_refresh_token(token: str) -> Optional[dict]:
    try:
        return jwt.decode(token, REFRESH_SECRET_KEY, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        raise ExpiredTokenError("expired token")
    except jwt.InvalidTokenError:
        raise InvalidTokenError("Invalid token")

def generate_token_pair(user_id: int, social_login: bool, email: str) -> dict:
    return {
        "access_token": create_access_token(user_id=user_id, social_login=social_login, email=email),
        "refresh_token": create_refresh_token(user_id=user_id, social_login=social_login, email=email),
    }
