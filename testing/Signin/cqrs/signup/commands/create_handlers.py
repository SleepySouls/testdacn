from cqrs.handlers import ICommandHandler
from repository.signup_repo import SignupRepository
from cqrs.signup.command import SignupCommand

class AddSignupCommandHandler(ICommandHandler): 
    
    def __init__(self): 
        self.repo:SignupRepository = SignupRepository()
        
    async def handle(self, command:SignupCommand) -> bool:
        result = await self.repo.create_signup_user(command.details)
        return result