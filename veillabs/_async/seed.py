from typing import Dict, Any, Union
from ..base import BaseAsyncSubClient
from ..models import SeedResponse, SeedRequest


class SeedSubClient(BaseAsyncSubClient):
    """
    Asynchronous sub-client for private seed distribution operations.
    """

    async def create(self, params: Union[SeedRequest, Dict[str, Any]]) -> SeedResponse:
        """
        Creates a new private seed distribution transaction.
        """
        if isinstance(params, dict):
            params = SeedRequest(**params)

        response = await self.http_client.post(
            f"{self.base_url}/seed/create",
            json=params.model_dump(by_alias=True, exclude_none=True),
        )
        self._raise_for_status(response)
        return SeedResponse(**response.json())

    async def get_status(self, seed_id: str) -> SeedResponse:
        """
        Retrieves the current status of a specific seed distribution.
        """
        response = await self.http_client.get(f"{self.base_url}/seed/status/{seed_id}")
        self._raise_for_status(response)
        return SeedResponse(**response.json())
