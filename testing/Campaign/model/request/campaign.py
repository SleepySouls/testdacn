from pydantic import BaseModel
from datetime import date

class CampaignReq(BaseModel):
    title: str
    description: str
    goal_amount: float
    raised_amount: float
    start_date: date
    end_date: date
    category: str
    media: bytes
    status: bool

    class Config:
        orm_mode = True