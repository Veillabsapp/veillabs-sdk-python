from typing import Dict, Any
from ..base import BaseAsyncSubClient
from ..models import TransferResponse

class TransferSubClient(BaseAsyncSubClient):
    """
    Asynchronous sub-client for secure proxy transfer operations.
    """
    async def single(self, **params) -> TransferResponse:
        """
        Creates a single private proxy transfer.
        """
        response = await self.http_client.post(f"{self.base_url}/transfer", json=params)
        response.raise_for_status()
        return TransferResponse(**response.json())

    async def multi(self, **params) -> TransferResponse:
        """
        Creates a multi-destination private proxy transfer.
        """
        response = await self.http_client.post(f"{self.base_url}/transfer/multi", json=params)
        response.raise_for_status()
        return TransferResponse(**response.json())
