from Core_layer.Bot_package.Interfaces import IUser
from Deep_layer.DB_package.Classes import DB_Communication

class User(IUser.IUser):

    __dbc = DB_Communication.DB_Communication()

    @classmethod
    def check(cls, user):

        return cls.__dbc.check(column='userr',table='white_list_of_users',input_string=user)