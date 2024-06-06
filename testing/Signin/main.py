from fastapi import FastAPI
from api import logout_api, signup_api, signin_api

app = FastAPI()
app.include_router(signup_api.router, prefix="/signup")
app.include_router(logout_api.router, prefix="/logout")
app.include_router(signin_api.router, prefix="/signin") 