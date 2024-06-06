from cqrs.handlers import ICommandHandler
from repository.signin_repo import SigninRepository
from cqrs.signin.command import SigninCommand

class AddSigninCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:SigninRepository = SigninRepository()
        
    async def handle(self, command:SigninCommand) -> bool:
        result = await self.repo.create_login_user(command.details)
        return result