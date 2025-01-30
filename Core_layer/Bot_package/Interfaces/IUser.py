from abc import ABC, abstractmethod

class IUser(ABC):
    """
    It is entity of tokens
    """

    @abstractmethod
    def check(cls, token):
        pass