from typing import Dict, Any
from ..base import BaseSyncSubClient
from ..models import SwapResponse

class SwapSubClient(BaseSyncSubClient):
    """
    Synchronous sub-client for private swap operations.
    """
    def create(self, **params) -> SwapResponse:
        """
        Creates a new private swap transaction.
        """
        response = self.http_client.post(f"{self.base_url}/exchanges", json=params)
        response.raise_for_status()
        return SwapResponse(**response.json())

    def get_status(self, swap_id: str) -> SwapResponse:
        """
        Retrieves the current status of a specific swap transaction.
        """
        response = self.http_client.get(f"{self.base_url}/exchanges/{swap_id}")
        response.raise_for_status()
        return SwapResponse(**response.json())
