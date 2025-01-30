import logging
import warnings
import pandas as pd
from multipledispatch import dispatch
from Deep_layer.DB_package.Classes import Connections
from Deep_layer.DB_package.Inerfaces import IDB_Communication


class DB_Communication(IDB_Communication.IDB_Communication):
    """
    It is class for communication with a data base
    """
    warnings.filterwarnings('ignore')

    @classmethod
    def get_data(cls, select):
#
#       Its a method for getting data from a database
        logging.basicConfig(level=logging.INFO, filename="imei.log", filemode="w")
        try:
            postgr_conn = Connections.PostgresConnection()
            df = pd.read_sql(select, postgr_conn.conn_remote)
            logging.info('The db_communication.get_data is done')
            return df
        except Exception as e:
            logging.exception(str('The exception is in db_communication.get_data ' + str(e)))


    @classmethod
    def checkcvalidimei(cls, input_string):
#
#       Its a method for checking of imei in a database
        logging.basicConfig(level=logging.INFO, filename="imei.log", filemode="w")
        try:
            postgr_conn = Connections.PostgresConnection()
            df = pd.read_sql('SELECT text FROM assistant_sets.validimei', postgr_conn.conn_remote)
            Cdict = df['text'].to_dict()

            input_array = input_string.split(' ')
            for cdictvalue in Cdict.values():
                for item in input_array:
                    if(cdictvalue == item):
                        logging.info('The db_communication.checkcvalidimei is done')
                        return True
            logging.info('The db_communication.checkcvalidimei is done')
            return False
        except Exception as e:
            logging.exception(str('The exception is in db_communication.checkcvalidimei ' + str(e)))


    @classmethod
    def checkuser(cls, input_string):
#
#       Its a method for checking of users in a database
        logging.basicConfig(level=logging.INFO, filename="imei.log", filemode="w")
        try:
            postgr_conn = Connections.PostgresConnection()
            df = pd.read_sql('SELECT userr FROM assistant_sets.white_list_of_users', postgr_conn.conn_remote)
            Cdict = df['userr'].to_dict()

            input_array = input_string.split(' ')
            for cdictvalue in Cdict.values():
                for item in input_array:
                    if (cdictvalue == item):
                        logging.info('The db_communication.checkcommands is done')
                        return True
            logging.info('The db_communication.checkuser is done')
            return False
        except Exception as e:
            logging.exception(str('The exception is in db_communication.checkuser ' + str(e)))