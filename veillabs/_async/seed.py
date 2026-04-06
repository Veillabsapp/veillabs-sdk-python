from typing import Dict, Any
from ..base import BaseAsyncSubClient
from ..models import SeedResponse

class SeedSubClient(BaseAsyncSubClient):
    """
    Asynchronous sub-client for private seed distribution operations.
    """
    async def create(self, **params) -> SeedResponse:
        """
        Creates a new private seed distribution transaction.
        """
        response = await self.http_client.post(f"{self.base_url}/seed/create", json=params)
        response.raise_for_status()
        return SeedResponse(**response.json())

    async def get_status(self, seed_id: str) -> SeedResponse:
        """
        Retrieves the current status of a specific seed distribution.
        """
        response = await self.http_client.get(f"{self.base_url}/seed/status/{seed_id}")
        response.raise_for_status()
        return SeedResponse(**response.json())
