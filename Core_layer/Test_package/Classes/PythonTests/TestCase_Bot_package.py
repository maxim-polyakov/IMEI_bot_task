import unittest
from Core_layer.Bot_package.Classes.Token import Token
from Core_layer.Test_package.Interfases import ITestCase


class TestCase_ValidsetAlanizer(ITestCase.ITestCase):
    """

    This class is written for testing entityes of system

    """
    def test_token(self):
        tkn = Token.Token()
        df = tkn.get_token(
            'select token from assistant_sets.tokens where botname = \'Imei\' and platformname = \'Telegram\'')
        pass

    def text_imei(self):
        pass
if __name__ == '__main__':
    unittest.main()
