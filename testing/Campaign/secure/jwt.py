from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, HTTPBasic
from jose import jwt, JWTError
import requests

brypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
http_basic = HTTPBasic()

SECRET_KEY = "tbWivbkVxfsuTxCP8A+Xg67LcmjXXl/sszHXwH+TX9w="
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://127.0.0.1:8000/signin/login_user/login", scheme_name="JWT")
def get_password_hash(password):
    return brypt_context.hash(password)

def verify_password(plain_password, hashed_password):
    return brypt_context.verify(plain_password, hashed_password)

def verify_user(username, exist_username):
    return (username == exist_username)

async def get_user_credentials():
    response = requests.get("http://127.0.0.1:8000/signin/login_user/list_user")
    response_data = response.json()
    usernames = response_data["usernames"]
    passwords = response_data["passwords"]
    users_id = response_data["users_id"]
    return usernames, passwords, users_id

def get_invalidated_token():
    response = requests.get("http://127.0.0.1:8000/logout/logout_user/invalidated_token")
    response_data = response.json()
    invalidated_tokens = response_data["invalidated_tokens"]
    return invalidated_tokens

def is_token_invalidated(token: str) -> bool:
    invalidated_token = get_invalidated_token()
    return token in invalidated_token

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    if is_token_invalidated(token):
        raise credentials_exception
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return {
            "username": username}
    except JWTError as e:
        print(f"JWT Error: {e}")
        raise credentials_exception
