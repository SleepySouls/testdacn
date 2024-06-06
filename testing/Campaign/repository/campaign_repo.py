from model.data.gino_model import Campaign
from typing import Dict, Any, List
from db_config.gino_connect import db
from sqlalchemy import func, Sequence

class CampaignRepository:

    async def create_campaign(self, details: Dict[str, Any]) -> bool:
        try:
            async with db.acquire() as conn:
                seq = Sequence('campaign_campaign_id_seq')
                id = await conn.scalar(func.next_value(seq))
                details['campaign_id'] = id
            await Campaign.create(**details)
            return True
        except Exception as e:
            print(f"Error creating campaign: {e}")
            return False
        

    async def update_campaign(self, title: str, details: Dict[str, Any]) -> bool:
        try:
            campaign = await Campaign.query.where(Campaign.title == title).gino.first()
            if campaign is not None:
                await campaign.update(**details).apply()
                return True
            else:
                print(f"No campaign with title '{title}' found")
                return False
        except Exception as e:
            print(f"Error updating campaign: {e}")
            return False

    async def delete_campaign(self, title: str) -> bool:
        try:
            campaign = await Campaign.query.where(Campaign.title == title).gino.first()
            if campaign is not None:
                await campaign.delete()
                return True
            else:
                print(f"No campaign with title '{title}' found")
                return False
        except Exception as e:
            print(f"Error deleting campaign: {e}")
            return False

    async def get_all_campaign(self, title: str = None) -> List[Dict[str, Any]]:
        try:
            query = Campaign.query.gino.all()
            if title:
                query = query.filter(Campaign.title == title)
            campaigns = await query
            return [camapaign.to_dict() for camapaign in campaigns]
        except Exception as e:
            print(f"Error retrieving all campaign: {e}")
            return []
        
    async def get_campaign_by_user_id(self, user_id: int):
        try:
            return await Campaign.get(user_id)
        except Exception as e:
            print(f"Error retrieving campaign: {e}")
            return None