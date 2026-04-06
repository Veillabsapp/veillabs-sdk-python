from typing import Dict, Any, Union
from ..base import BaseAsyncSubClient
from ..models import SwapResponse, SwapRequest


class SwapSubClient(BaseAsyncSubClient):
    """
    Asynchronous sub-client for private swap operations.
    """

    async def create(self, params: Union[SwapRequest, Dict[str, Any]]) -> SwapResponse:
        """
        Creates a new private swap transaction.
        """
        if isinstance(params, dict):
            params = SwapRequest(**params)

        response = await self.http_client.post(
            f"{self.base_url}/exchanges",
            json=params.model_dump(by_alias=True, exclude_none=True),
        )
        self._raise_for_status(response)
        return SwapResponse(**response.json())

    async def get_status(self, swap_id: str) -> SwapResponse:
        """
        Retrieves the current status of a specific swap transaction.
        """
        response = await self.http_client.get(f"{self.base_url}/exchanges/{swap_id}")
        self._raise_for_status(response)
        return SwapResponse(**response.json())
