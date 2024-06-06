from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from db_config.gino_connect import sess_db
from model.request.user_signup import UserSignUpReq
from cqrs.signup.commands.create_handlers import AddSignupCommandHandler
from cqrs.signup.command import SignupCommand
from secure.jwt import get_password_hash

    
router = APIRouter(dependencies=[Depends(sess_db)])


@router.post("/signup/add", tags=['Signup'] )
async def add_signup_user(req: UserSignUpReq): 
    handler = AddSignupCommandHandler()
    signup_user_profile = dict()
    signup_user_profile["username"] = req.username
    signup_user_profile["hashed_password"] = get_password_hash(req.password)
    signup_user_profile["email"] = req.email
    signup_user_profile["first_name"] = req.first_name
    signup_user_profile["last_name"] = req.last_name
    command = SignupCommand()
    command.details = signup_user_profile
    result = await handler.handle(command)
    if result == True: 
        return req 
    else: 
        return JSONResponse(content={'message':'create signup user profile problem encountered'}, status_code=500) 