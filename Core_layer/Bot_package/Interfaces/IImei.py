from abc import ABC, abstractmethod

class IImei(ABC):

    @abstractmethod
    def get_imei(cls):
        pass
