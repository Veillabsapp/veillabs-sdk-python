from typing import Dict, Any, Union
from ..base import BaseSyncSubClient
from ..models import SwapResponse, SwapRequest


class SwapSubClient(BaseSyncSubClient):
    """
    Synchronous sub-client for private swap operations.
    """

    def create(self, params: Union[SwapRequest, Dict[str, Any]]) -> SwapResponse:
        """
        Creates a new private swap transaction.
        """
        if isinstance(params, dict):
            params = SwapRequest(**params)

        response = self.http_client.post(
            f"{self.base_url}/exchanges", json=params.model_dump(by_alias=True)
        )
        response.raise_for_status()
        return SwapResponse(**response.json())

    def get_status(self, swap_id: str) -> SwapResponse:
        """
        Retrieves the current status of a specific swap transaction.
        """
        response = self.http_client.get(f"{self.base_url}/exchanges/{swap_id}")
        response.raise_for_status()
        return SwapResponse(**response.json())
