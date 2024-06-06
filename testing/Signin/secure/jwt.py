from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, HTTPBasic
from jose import jwt, JWTError
from cqrs.user.query.query_handlers import ListUserQueryHandler
from cqrs.user.queries import UserListQuery

from datetime import datetime, timedelta, timezone

brypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
http_basic = HTTPBasic()

SECRET_KEY = "tbWivbkVxfsuTxCP8A+Xg67LcmjXXl/sszHXwH+TX9w="
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/signin/login_user/login", scheme_name="JWT")
invalidated_tokens = set() 
def get_password_hash(password):
    return brypt_context.hash(password)

def verify_password(plain_password, hashed_password):
    return brypt_context.verify(plain_password, hashed_password)

def verify_user(username, exist_username):
    return (username == exist_username)

async def get_user_credentials():
    handler = ListUserQueryHandler()
    query:UserListQuery = await handler.handle() 
    records = query.records
    usernames = [record['username'] for record in records]
    passwords = [record['hashed_password'] for record in records]
    return {'usernames': usernames, 'passwords': passwords}

async def authenticate(username, password):
    try:
        account = await get_user_credentials()
        if account is None:
            return False
        usernames = account['usernames']
        passwords = account['passwords']
        if username not in usernames:
            return False
        index = usernames.index(username)
        if not verify_password(password, passwords[index]):
            return False
        return True
    except Exception as e:
        print(e)
        return False
def create_access_token(data: dict, expires_after: timedelta):
    plain_text = data.copy()
    expire = datetime.now(timezone.utc) + expires_after
    plain_text.update({"exp": expire})
    encoded_jwt = jwt.encode(plain_text, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
       
async def logout(token):
    try:
        invalidated_tokens.add(token)
        return {"msg": "Logout successful"}
    except JWTError as e:
        print(f"JWT Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
def is_token_invalidated(token: str) -> bool:
    return token in invalidated_tokens

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
            "username": username
            }
    except JWTError as e:
        print(f"JWT Error: {e}")
        raise credentials_exception