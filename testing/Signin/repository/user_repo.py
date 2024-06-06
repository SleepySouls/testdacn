from model.data.gino_model import User
from typing import Dict, Any, List

class UserRepository:
    async def update_user(self, username: str, details: Dict[str, Any]) -> bool:
        try:
            user = await User.query.where(User.username == username).gino.first()
            if user is not None:
                await user.update(**details).apply()
                return True
            else:
                print(f"No user with username '{username}' found")
                return False
        except Exception as e:
            print(f"Error updating user: {e}")
            return False

    async def delete_user(self, username: str) -> bool:
        try:
            user = await User.query.where(User.username == username).gino.first()
            if user is not None:
                await user.delete()
                return True
            else:
                print(f"No user with username '{username}' found")
                return False
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False

    async def get_all_users(self, username: str = None) -> List[Dict[str, Any]]:
        try:
            query = User.query.gino.all()
            if username:
                query = query.filter(User.username == username)
            users = await query
            return [user.to_dict() for user in users]
        except Exception as e:
            print(f"Error retrieving all login users: {e}")
            return []
        
    async def get_user_id_by_username(self, username: str) -> int:
        try:
            user = await User.query.where(User.username == username).gino.first()
            if user is not None:
                return user.user_id
            else:
                print(f"No user id with username '{username}' found")
                return None
        except Exception as e:
            print(f"Error getting user id: {e}")
            return None