from flask_login import UserMixin
from website.func import get_user_by_id

class UserLogin(UserMixin):
    def fromDB(self, user_id):
        self.__user = get_user_by_id(user_id)
        return self

    def create(self, user):
        self.__user = user
        return self

    def get_id(self):
        return str(self.__user.user_id)
    
    def get_name(self):
        return str(self.__user.name)
    
    def has_role(self, role):
        user_role = self.__user.has_role(role)
        return user_role
