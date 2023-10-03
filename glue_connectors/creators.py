"""
Create concrete connector objects.
"""

from glue_connectors.connection import ConnectionCreator
from glue_connectors.opensearch.connector import OpenSearchConnector
from glue_connectors.trino.connector import TrinoConnector


class OpenSearchConnectionCreator(ConnectionCreator):
    """
    Concrete creator class that extends the ConnectionCreator class.
    """

    def build_connection(self, **kwargs) -> OpenSearchConnector:
        """
        Factory method that returns a OpenSearchConnector object.
        :param **kwargs:
        """
        return OpenSearchConnector(**kwargs)


class TrinoConnectionCreator(ConnectionCreator):
    """
    Concrete creator class that extends the ConnectionCreator class.
    """

    def build_connection(self, **kwargs) -> TrinoConnector:
        """
        Factory method that returns a TrinoConnector object.
        :param **kwargs:
        """
        return TrinoConnector()


def get_connector(connector_type: str) -> ConnectionCreator:
    """
    Factory method that returns a Connector object.
    """
    supported_connectors = {
        "opensearch": OpenSearchConnectionCreator(),
        "trino": TrinoConnectionCreator(),
    }
    if connector_type in supported_connectors:
        return supported_connectors[connector_type]
    else:
        raise ValueError(f"Unsupported connector type: {connector_type}")
