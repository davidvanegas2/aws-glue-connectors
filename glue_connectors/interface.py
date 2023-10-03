"""
Interfaces required to instantiate each of the connector objects.

The glue_connectors package is a collection of classes that implement the
interfaces defined in this module.
"""

from abc import ABC, abstractmethod


class IConnector(ABC):
    """
    The IConnector interface declares methods common to all concrete connector classes.
    """

    @abstractmethod
    def connect(self) -> None:
        """
        Connect to the source and destination.
        """
        pass

    @abstractmethod
    def disconnect(self) -> None:
        """
        Disconnect from the source and destination.
        """
        pass
