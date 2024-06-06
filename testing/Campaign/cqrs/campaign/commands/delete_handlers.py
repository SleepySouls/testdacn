from cqrs.handlers import ICommandHandler
from repository.campaign_repo import CampaignRepository
from cqrs.campaign.command import CampaignCommand

class DeleteCampaignCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:CampaignRepository = CampaignRepository()
    
        
    async def handle(self, command:CampaignCommand) -> bool:
        result = await self.repo.delete_campaign(command.details.get("id"))
        return result
