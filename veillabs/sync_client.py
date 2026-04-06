from typing import Dict, Any
import httpx
from ._sync.market import MarketSubClient
from ._sync.swap import SwapSubClient
from ._sync.seed import SeedSubClient
from ._sync.transfer import TransferSubClient
from ._sync.stats import StatsSubClient
from .models import TrackingResponse

class VeilLabsClient:
    """
    Synchronous client for the Veil Labs API.
    """
    def __init__(self, base_url: str = "https://trade.veillabs.app/api"):
        """
        Initializes the synchronous Veil Labs client.
        
        Args:
            base_url: The base API URL.
        """
        self.base_url = base_url
        self._http_client = httpx.Client()
        self.market = MarketSubClient(self)
        self.swap = SwapSubClient(self)
        self.seed = SeedSubClient(self)
        self.transfer = TransferSubClient(self)
        self.stats = StatsSubClient(self)

    def track(self, tracking_id: str) -> TrackingResponse:
        """
        Retrieves the status of any transaction using its tracking ID.
        """
        response = self._http_client.get(f"{self.base_url}/tracking/{tracking_id}")
        response.raise_for_status()
        return TrackingResponse(**response.json())

    def close(self):
        """
        Closes the underlying HTTP client.
        """
        self._http_client.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
