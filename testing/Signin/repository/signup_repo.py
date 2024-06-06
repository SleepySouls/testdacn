from model.data.gino_model import User
from typing import Dict, Any, List
from sqlalchemy import func, Sequence
from db_config.gino_connect import db
class SignupRepository:

    async def create_signup_user(self, details: Dict[str, Any]) -> bool:
        try:
            async with db.acquire() as conn:
                seq = Sequence('user_user_id_seq')
                id = await conn.scalar(func.next_value(seq))
                details['user_id'] = id
            await User.create(**details)
            return True
        except Exception as e:
            print(f"Error in signing up user: {e}")
            return False
        
    # async def update_signup_user(self, username: str, details: Dict[str, Any]) -> bool:
    #     try:
    #         user = await User.query.where(User.username == username).gino.first()
    #         if user is not None:
    #             await user.update(**details).apply()
    #             return True
    #         else:
    #             print(f"No user with username '{username}' found")
    #             return False
    #     except Exception as e:
    #         print(f"Error updating user: {e}")
    #         return False
        
    # async def delete_signup_user(self, username: str) -> bool:
    #     try:
    #         user = await User.query.where(User.username == username).gino.first()
    #         if user is not None:
    #             await user.delete()
    #             return True
    #         else:
    #             print(f"No user with username '{username}' found")
    #             return False
    #     except Exception as e:
    #         print(f"Error deleting user: {e}")
    #         return False

    # async def get_all_signup_users(self, username: str = None) -> List[Dict[str, Any]]:
    #     try:
    #         query = User.query.gino.all()
    #         if username:
    #             query = query.filter(User.username == username)
    #         users = await query
    #         return [user.to_dict() for user in users]
    #     except Exception as e:
    #         print(f"Error retrieving all login users: {e}")
    #         return []