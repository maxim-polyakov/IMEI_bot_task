from Deep_layer.DB_package.Classes import DB_Communication
from Deep_layer.API_package.Classes import Imei
from Core_layer.Bot_package.Interfaces import IImei


class Imei(IImei.IImei):
    """

    This class describes object of taking monitors from a database

    """
    __dbc = DB_Communication.DB_Communication()
    text = None
    __im = Imei.Imei()

    def __init__(self, text):
        Imei.text = text

    @classmethod
    def get_imei(cls):
        if(cls.__dbc.check(column='text',table='validimei', input_string=cls.text)):
            res = cls.__im.get_imei_info(cls.text)
            return res
