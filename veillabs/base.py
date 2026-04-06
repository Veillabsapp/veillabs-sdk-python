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

    def _raise_for_status(self, response: httpx.Response):
        """
        Custom status check that provides more detailed error messages
        from the Veil Labs API when available.
        """
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            if response.status_code == 400:
                try:
                    error_data = response.json()
                    message = error_data.get(
                        "message", error_data.get("error", response.text)
                    )
                    raise ValueError(
                        f"Veil Labs API Error (400 Bad Request): {message}"
                    ) from e
                except Exception:
                    pass
            raise e

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
