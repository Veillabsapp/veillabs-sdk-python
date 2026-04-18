import httpx
from ._async.market import MarketSubClient
from ._async.swap import SwapSubClient
from ._async.seed import SeedSubClient
from ._async.stats import StatsSubClient
from .models import TrackingResponse


class AsyncVeilLabsClient:
    """
    Asynchronous client for the Veil Labs API.
    """

    def __init__(self, base_url: str = "https://trade.veillabs.app/api"):
        """
        Initializes the asynchronous Veil Labs client.

        Args:
            base_url: The base API URL.
        """
        self.base_url = base_url
        self._http_client = httpx.AsyncClient()
        self.market = MarketSubClient(self)
        self.swap = SwapSubClient(self)
        self.seed = SeedSubClient(self)
        self.stats = StatsSubClient(self)

    async def track(self, tracking_id: str) -> TrackingResponse:
        """
        Retrieves the status of any transaction using its tracking ID.
        """
        response = await self._http_client.get(
            f"{self.base_url}/tracking/{tracking_id}"
        )
        response.raise_for_status()
        return TrackingResponse(**response.json())

    async def close(self):
        """
        Closes the underlying HTTP client.
        """
        await self._http_client.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
