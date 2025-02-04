from Deep_layer.API_package.Interfaces import IImei
from Deep_layer.DB_package.Classes import DB_Communication
import os
import platform
import json

import requests
class Imei(IImei.IImei):


    __dbc = DB_Communication.DB_Communication()
    @classmethod
    def get_imei_info(cls, imei):
        url = "https://alpha.imeicheck.com/api/modelBrandName?imei=" + str(imei) + "&format=json"
        response_API = requests.get(url, verify=False)
        data = response_API.json()
        return data
