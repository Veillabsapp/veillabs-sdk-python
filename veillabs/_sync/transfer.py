from typing import Dict, Any, Union
from ..base import BaseSyncSubClient
from ..models import TransferResponse, TransferRequest, MultiTransferRequest


class TransferSubClient(BaseSyncSubClient):
    """
    Synchronous sub-client for secure proxy transfer operations.
    """

    def single(
        self, params: Union[TransferRequest, Dict[str, Any]]
    ) -> TransferResponse:
        """
        Creates a single private proxy transfer.
        """
        if isinstance(params, dict):
            params = TransferRequest(**params)

        response = self.http_client.post(
            f"{self.base_url}/transfer",
            json=params.model_dump(by_alias=True, exclude_none=True),
        )
        self._raise_for_status(response)
        return TransferResponse(**response.json())

    def multi(
        self, params: Union[MultiTransferRequest, Dict[str, Any]]
    ) -> TransferResponse:
        """
        Creates a multi-destination private proxy transfer.
        """
        if isinstance(params, dict):
            params = MultiTransferRequest(**params)

        response = self.http_client.post(
            f"{self.base_url}/transfer/multi",
            json=params.model_dump(by_alias=True, exclude_none=True),
        )
        self._raise_for_status(response)
        return TransferResponse(**response.json())
