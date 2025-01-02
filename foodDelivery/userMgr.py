from user import User
import threading

class UserManager:
    _userManagerInstance = None
    _mtx = threading.Lock()

    def __init__(self) -> None:
        self.user_list = {}
    
    @staticmethod
    def get_user_manager_instance():
        if UserManager._userManagerInstance is None:
            with UserManager._mtx:
                if UserManager._userManagerInstance is None:
                    UserManager._userManagerInstance = UserManager()
        return UserManager._userManagerInstance
        
    def add_user(self, user: User) -> None:
        self.user_list[user.get_user_id()] = user

    def get_user(self, userId) -> User:
        return self.user_list[userId]
