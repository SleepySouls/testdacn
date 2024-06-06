from pydantic import BaseModel

class UserSignUpReq(BaseModel):
    username: str
    password: str 
    email: str 
    first_name: str 
    last_name: str 
    class Config:
        orm_mode = True

