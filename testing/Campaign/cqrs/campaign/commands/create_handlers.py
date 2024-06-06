from cqrs.handlers import ICommandHandler
from repository.campaign_repo import CampaignRepository
from cqrs.campaign.command import CampaignCommand

class AddCampaignCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:CampaignRepository = CampaignRepository()
        
    async def handle(self, command:CampaignCommand) -> bool:
        result = await self.repo.create_campaign(command.details)
        return result