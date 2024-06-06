from cqrs.handlers import ICommandHandler
from repository.user_repo import UserRepository
from cqrs.user.command import UserCommand

class UpdateUserCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:UserRepository = UserRepository()
        
    async def handle(self, command:UserCommand) -> bool:
        id = command.details['id']
        details = {key: value for key, value in command.details.items() if key != 'id'}
        result = await self.repo.update_user(id, details)
        return result