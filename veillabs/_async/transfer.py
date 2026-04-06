from typing import Dict, Any, Union
from ..base import BaseAsyncSubClient
from ..models import TransferResponse, TransferRequest, MultiTransferRequest


class TransferSubClient(BaseAsyncSubClient):
    """
    Asynchronous sub-client for secure proxy transfer operations.
    """

    async def single(
        self, params: Union[TransferRequest, Dict[str, Any]]
    ) -> TransferResponse:
        """
        Creates a single private proxy transfer.
        """
        if isinstance(params, dict):
            params = TransferRequest(**params)

        response = await self.http_client.post(
            f"{self.base_url}/transfer", json=params.model_dump(by_alias=True)
        )
        response.raise_for_status()
        return TransferResponse(**response.json())

    async def multi(
        self, params: Union[MultiTransferRequest, Dict[str, Any]]
    ) -> TransferResponse:
        """
        Creates a multi-destination private proxy transfer.
        """
        if isinstance(params, dict):
            params = MultiTransferRequest(**params)

        response = await self.http_client.post(
            f"{self.base_url}/transfer/multi", json=params.model_dump(by_alias=True)
        )
        response.raise_for_status()
        return TransferResponse(**response.json())
