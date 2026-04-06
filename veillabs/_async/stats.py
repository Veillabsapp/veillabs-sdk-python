from typing import Dict, Any
from ..base import BaseAsyncSubClient
from ..models import VolumeResponse

class StatsSubClient(BaseAsyncSubClient):
    """
    Asynchronous sub-client for accessing platform global metrics.
    """
    async def get_volume(self) -> VolumeResponse:
        """
        Retrieves total trade volume in USD for the platform.
        """
        response = await self.http_client.get(f"{self.base_url}/volume")
        response.raise_for_status()
        return VolumeResponse(**response.json())
