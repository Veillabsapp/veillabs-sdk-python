from typing import Dict, Any
from ..base import BaseSyncSubClient
from ..models import TransferResponse

class TransferSubClient(BaseSyncSubClient):
    """
    Synchronous sub-client for secure proxy transfer operations.
    """
    def single(self, **params) -> TransferResponse:
        """
        Creates a single private proxy transfer.
        """
        response = self.http_client.post(f"{self.base_url}/transfer", json=params)
        response.raise_for_status()
        return TransferResponse(**response.json())

    def multi(self, **params) -> TransferResponse:
        """
        Creates a multi-destination private proxy transfer.
        """
        response = self.http_client.post(f"{self.base_url}/transfer/multi", json=params)
        response.raise_for_status()
        return TransferResponse(**response.json())
