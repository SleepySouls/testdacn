from fastapi import APIRouter, Depends, HTTPException
from db_config.gino_connect import sess_db
from model.request.user_signin import UserSignInReq
from secure.jwt import authenticate, create_access_token, get_current_user, get_user_credentials
from datetime import timedelta
from model.request.tokens import Token
from cqrs.user.query.query_handlers import RecordUserQueryHandler
from cqrs.user.queries import UserRecordQuery

router = APIRouter(dependencies=[Depends(sess_db)])

@router.post("/login_user/login", response_model=Token, tags=['Login'] )
async def login(req: UserSignInReq):
    username = req.username
    password = req.password
    if await authenticate(username, password) == True:
        access_token = create_access_token(data={"sub": username}, expires_after=timedelta(minutes=20))
        return {"access_token": access_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Incorrect username or password or you are not a registered user")
    
@router.get("/login_user/get_current_user", tags=['Login'])
async def get_current_user(current_user: dict = Depends(get_current_user)):
    return current_user

@router.get("/login_user/list_user", tags=['Login'])
async def list_users(): 
    credentials =  await get_user_credentials()
    if credentials:
        return credentials
    else:
        return {"message": "No users found"}
    
# @router.get("/login_user/get_current_user_id", tags=['Login'])
# async def get_current_user_id(current_user: dict = Depends(get_current_user)):
#     username = current_user.get("username")
#     handler = RecordUserQueryHandler()
#     query:UserRecordQuery = await handler.handle(username)
#     return query.record
@router.get("/login_user/get_current_user_id", tags=['Login'])
async def get_current_user_id(current_user: str):
    handler = RecordUserQueryHandler()
    query:UserRecordQuery = await handler.handle(current_user)
    return query.record