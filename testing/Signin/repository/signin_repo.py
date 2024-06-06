from model.data.gino_model import User
from typing import Dict, Any

class SigninRepository:

    async def create_login_user(self, details: Dict[str, Any]) -> bool:
        try:
            await User.create(**details)
            return True
        except Exception as e:
            print(f"Error in logging in: {e}")
            return False
        
        
    # async def update_login_user(self, username: str, details: Dict[str, Any]) -> bool:
    #     try:
    #         user = await Signin.query.where(Signin.username == username).gino.first()
    #         if user is not None:
    #             await user.update(**details).apply()
    #             return True
    #         else:
    #             print(f"No user with username '{username}' found")
    #             return False
    #     except Exception as e:
    #         print(f"Error updating login user: {e}")
    #         return False

    # async def delete_login_user(self, username: str) -> bool:
    #     try:
    #         user = await Signin.query.where(Signin.username == username).gino.first()
    #         if user is not None:
    #             await user.delete()
    #             return True
    #         else:
    #             print(f"No user with username '{username}' found")
    #             return False
    #     except Exception as e:
    #         print(f"Error deleting login user: {e}")
    #         return False
    
    # async def get_login_user_by_id(self, id: int):
    #     try:
    #         return await Signin.get(id)
    #     except Exception as e:
    #         print(f"Error retrieving login user: {e}")
    #         return None
        
    # async def get_all_login_users(self, username: str = None) -> List[Dict[str, Any]]:
    #     try:
    #         query = Signin.query.gino.all()
    #         if username:
    #             query = query.filter(Signin.username == username)
    #         users = await query
    #         return [user.to_dict() for user in users]
    #     except Exception as e:
    #         print(f"Error retrieving all login users: {e}")
    #         return []