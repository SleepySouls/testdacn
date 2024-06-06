from cqrs.handlers import ICommandHandler
from repository.user_repo import UserRepository
from cqrs.user.command import UserCommand


class DeleteUserCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:UserRepository = UserRepository()
    
        
    async def handle(self, command:UserCommand) -> bool:
        result = await self.repo.delete_user(command.details.get("id"))
        return result
