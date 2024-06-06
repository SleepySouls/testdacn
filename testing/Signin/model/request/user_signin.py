from pydantic import BaseModel

class UserSignInReq(BaseModel): 
    username: str 
    password: str    
    