import unittest
from Core_layer.Test_package.Interfases import ITestCase
from Deep_layer.API_package.Classes import Imei

class TestCase_API_package(ITestCase.ITestCase):
    """

    This class is written for testing entityes of system

    """
    __im = Imei.Imei()
    def test_imei(self):
        res = self.__im.get_imei()
        pass

if __name__ == '__main__':
    unittest.main()
