from cqrs.handlers import ICommandHandler
from repository.campaign_repo import CampaignRepository
from cqrs.campaign.command import CampaignCommand

class UpdateCampaignCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:CampaignRepository = CampaignRepository()
        
    async def handle(self, command:CampaignCommand) -> bool:
        title = command.details['title']
        details = {key: value for key, value in command.details.items() if key != 'title'}
        result = await self.repo.update_campaign(title, details)
        return result