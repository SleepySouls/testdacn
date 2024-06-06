from fastapi import Depends, HTTPException
from fastapi import APIRouter, Depends
from db_config.gino_connect import sess_db
from secure.jwt import logout, oauth2_scheme, invalidated_tokens

router = APIRouter(dependencies=[Depends(sess_db)])
@router.post("/logout_user/logout")
async def logout_user(token: str = Depends(oauth2_scheme)):
    try:
        result = await logout(token)
        return result
    except Exception as e:
        print(f"Error during logout: {str(e)}")
        raise HTTPException(status_code=500, detail="Logout failed")
    
@router.get("/logout_user/invalidated_token")
async def get_invalidated_token():
    return {"invalidated_tokens": list(invalidated_tokens)}