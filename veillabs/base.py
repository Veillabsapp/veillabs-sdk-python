from typing import TYPE_CHECKING, Union
import httpx

if TYPE_CHECKING:
    from .sync_client import VeilLabsClient
    from .async_client import AsyncVeilLabsClient


class BaseSubClient:
    """
    Base class for all functional sub-clients in the SDK.
    """

    def __init__(self, client: Union["VeilLabsClient", "AsyncVeilLabsClient"]):
        """
        Initializes a sub-client with a reference to the main SDK client.

        Args:
            client: The main VeilLabsClient or AsyncVeilLabsClient instance.
        """
        self.client = client

    @property
    def base_url(self) -> str:
        """
        Returns the base API URL from the main client.
        """
        return self.client.base_url


class BaseAsyncSubClient(BaseSubClient):
    """
    Base class for asynchronous sub-clients.
    """

    @property
    def http_client(self) -> httpx.AsyncClient:
        """
        Returns the shared httpx.AsyncClient instance.
        """
        return self.client._http_client


class BaseSyncSubClient(BaseSubClient):
    """
    Base class for synchronous sub-clients.
    """

    @property
    def http_client(self) -> httpx.Client:
        """
        Returns the shared httpx.Client instance.
        """
        return self.client._http_client
