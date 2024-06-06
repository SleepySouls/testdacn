from fastapi import FastAPI
from api import campaign_api

app = FastAPI()
app.include_router(campaign_api.router, prefix="/campaign")