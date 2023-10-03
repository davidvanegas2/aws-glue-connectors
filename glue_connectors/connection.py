"""
Factory Method
"""

from abc import ABC, abstractmethod


class ConnectionCreator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Connector class.
    """

    @abstractmethod
    def build_connection(self, **kwargs):
        """
        Factory method that returns a Connector object.
        :param **kwargs:
        """
        pass

    def get_connection(self, **kwargs):
        """
        Connect to the source and destination.
        """
        connector = self.build_connection(**kwargs)
        connector.connect()
        return connector
