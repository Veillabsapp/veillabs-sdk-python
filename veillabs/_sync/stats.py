from ..base import BaseSyncSubClient
from ..models import VolumeResponse


class StatsSubClient(BaseSyncSubClient):
    """
    Synchronous sub-client for accessing platform global metrics.
    """

    def get_volume(self) -> VolumeResponse:
        """
        Retrieves total trade volume in USD for the platform.
        """
        response = self.http_client.get(f"{self.base_url}/volume")
        self._raise_for_status(response)
        return VolumeResponse(**response.json())
