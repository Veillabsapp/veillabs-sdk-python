from typing import Dict, Any, Union
from ..base import BaseSyncSubClient
from ..models import SeedResponse, SeedRequest


class SeedSubClient(BaseSyncSubClient):
    """
    Synchronous sub-client for private seed distribution operations.
    """

    def create(self, params: Union[SeedRequest, Dict[str, Any]]) -> SeedResponse:
        """
        Creates a new private seed distribution transaction.
        """
        if isinstance(params, dict):
            params = SeedRequest(**params)

        response = self.http_client.post(
            f"{self.base_url}/seed/create", json=params.model_dump(by_alias=True)
        )
        response.raise_for_status()
        return SeedResponse(**response.json())

    def get_status(self, seed_id: str) -> SeedResponse:
        """
        Retrieves the current status of a specific seed distribution.
        """
        response = self.http_client.get(f"{self.base_url}/seed/status/{seed_id}")
        response.raise_for_status()
        return SeedResponse(**response.json())
