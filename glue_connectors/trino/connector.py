"""
Connector class that extends the IConnector interface. This class is the
responsible for connecting to Trino.
"""

from glue_connectors.interface import IConnector


class TrinoConnector(IConnector):
    """
    Concrete connector class that implements the IConnector interface.
    """

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def connect(self) -> None:
        """
        Connect to Trino.
        """
        print("Connecting to Trino")

    def disconnect(self) -> None:
        """
        Disconnect from Trino.
        """
        print("Disconnecting from Trino")
