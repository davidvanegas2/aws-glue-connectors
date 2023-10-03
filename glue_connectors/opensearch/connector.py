"""
Connector class that extends the IConnector interface. This class is the
responsible for connecting to OpenSearch.
"""

from opensearchpy import OpenSearch
from pyspark.sql import DataFrame

from glue_connectors.interface import IConnector


class OpenSearchConnector(IConnector):
    """
    Concrete connector class that implements the IConnector interface.
    """

    def __init__(self, endpoint: str = "opensearch-node1", port: int = 9200, **kwargs):
        self.endpoint = endpoint
        self.port = port

        # Get the kwargs
        self.ssl = kwargs.get("ssl", True)
        self.verify_certs = kwargs.get("verify_certs", False)
        self.username = kwargs.get("username", "admin")
        self.password = kwargs.get("password", "admin")
        self.nodes_wan_only = kwargs.get("nodes_wan_only", True)
        self.resource = kwargs.get("resource", "demo_index")

        # Define the OpenSearch client object as empty
        self.client = None

    # Magic methods
    def __str__(self):
        return (
            f"OpenSearchConnector"
            f"(endpoint={self.endpoint}, "
            f"port={self.port}, "
            f"ssl={self.ssl}, "
            f"verify_certs={self.verify_certs}, "
            f"username={self.username}, "
            f"password={self.password}, "
            f"nodes_wan_only={self.nodes_wan_only}, "
            f"resource={self.resource})"
        )

    # Getters and setters using property decorator
    @property
    def endpoint(self) -> str:
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint: str) -> None:
        self._endpoint = endpoint

    @property
    def port(self) -> int:
        return self._port

    @port.setter
    def port(self, port: int) -> None:
        self._port = port

    @property
    def ssl(self) -> bool:
        return self._ssl

    @ssl.setter
    def ssl(self, ssl: bool) -> None:
        self._ssl = ssl

    @property
    def verify_certs(self) -> bool:
        return self._verify_certs

    @verify_certs.setter
    def verify_certs(self, verify_certs: bool) -> None:
        self._verify_certs = verify_certs

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, username: str) -> None:
        self._username = username

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    def connect(self) -> OpenSearch:
        """
        Method to connect to OpenSearch using the OpenSearch client and return the client object.
        :return: OpenSearch client object.
        """
        print("Connecting to OpenSearch")
        self.client = OpenSearch(
            hosts=[{"host": self.endpoint, "port": self.port}],
            http_auth=(self.username, self.password),
            use_ssl=self.ssl,
            verify_certs=self.verify_certs,
            ssl_show_warn=False
        )

        return self.client

    def disconnect(self) -> None:
        """
        Disconnect from OpenSearch.
        """
        print("Disconnecting from OpenSearch")

    def ping(self) -> bool:
        """
        Ping OpenSearch.
        :return: True if OpenSearch is up and running, False otherwise.
        """
        if self.client is None:
            raise Exception("OpenSearch client is not connected.")
        return self.client.ping()

    def write_dataframe(self, df: DataFrame, index: str = "", mode: str = "overwrite") -> None:
        """
        Write a dataframe to OpenSearch.
        :param df: Dataframe to write to OpenSearch.
        :param index: Index to write the dataframe to. If not specified, the resource name will be used.
        :param mode: Write mode. Default is overwrite.
        :return: None
        """
        if index:
            self.resource = index

        self.check_compatibility()

        es_write_conf = self.get_os_write_conf()
        df.write.format("org.elasticsearch.spark.sql").options(**es_write_conf).mode(mode).save()

    def get_os_write_conf(self):
        """
        Get the OpenSearch write configuration to write a Spark dataframe to OpenSearch.
        :return: OpenSearch write configuration.
        """
        es_write_conf = {
            "es.nodes": self.endpoint,
            "es.port": str(self.port),
            "es.resource": self.resource,
            "es.nodes.wan.only": str(self.nodes_wan_only).lower(),
            "es.net.http.auth.user": self.username,
            "es.net.http.auth.pass": self.password,
            "es.net.ssl": str(self.ssl).lower(),
            "es.net.ssl.cert.allow.self.signed": "true",
            "es.index.auto.create": "true",
        }
        return es_write_conf

    def get_os_settings(self) -> dict:
        """
        Get the OpenSearch settings.
        :return: OpenSearch settings.
        """
        return self.client.cluster.get_settings(include_defaults=True)

    def update_os_settings(self, settings: dict) -> None:
        """
        Update the OpenSearch cluster settings.
        :param settings: OpenSearch settings.
        :return: None
        """
        self.client.cluster.put_settings(body=settings)
        print("OpenSearch cluster settings updated.")

    def check_compatibility(self) -> None:
        """
        Check if the OpenSearch version is compatible with the connector. If not, update the cluster settings.
        :return: None
        """
        settings = {
            "persistent": {
                "compatibility": {
                    "override_main_response_version": "true"
                }
            }
        }
        cluster_settings = self.get_os_settings()

        # Extract the relevant setting value
        current_setting = cluster_settings.get("defaults", {}).get("compatibility", {}).get(
            "override_main_response_version") or \
                          cluster_settings.get("persistent", {}).get("compatibility", {}).get(
                              "override_main_response_version")

        if current_setting == "false":
            self.update_os_settings(settings)
