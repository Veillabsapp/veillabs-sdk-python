from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, ConfigDict


class Currency(BaseModel):
    """
    Representation of a cryptocurrency available on the platform.

    Attributes:
        ticker: Currency ticker symbol (e.g., 'eth').
        name: Full name of the currency.
        network: Blockchain network (e.g., 'mainnet', 'bsc').
        is_featured: Whether the currency is a featured asset.
        image: URL to the currency icon.
    """

    model_config = ConfigDict(populate_by_name=True)

    ticker: str
    name: str
    network: str
    is_featured: bool = Field(alias="isFeatured", default=False)
    image: Optional[str] = None


class Pair(BaseModel):
    """
    Available trade pair between two cryptocurrencies.

    Attributes:
        from_ticker: Source currency ticker.
        to_ticker: Target currency ticker.
        from_network: Source blockchain network.
        to_network: Target blockchain network.
    """

    model_config = ConfigDict(populate_by_name=True)

    from_ticker: str = Field(alias="fromTicker")
    to_ticker: str = Field(alias="toTicker")
    from_network: str = Field(alias="fromNetwork")
    to_network: str = Field(alias="toNetwork")


class EstimateRequest(BaseModel):
    """
    Request parameters for an exchange estimate.

    Attributes:
        from_ticker: Source currency ticker.
        to_ticker: Target currency ticker.
        from_amount: Input amount.
        from_network: Source blockchain network.
        to_network: Target blockchain network.
    """

    model_config = ConfigDict(populate_by_name=True)

    from_ticker: str = Field(alias="fromTicker")
    to_ticker: str = Field(alias="toTicker")
    from_amount: str = Field(alias="fromAmount")
    from_network: str = Field(alias="fromNetwork")
    to_network: str = Field(alias="toNetwork")


class Estimate(BaseModel):
    """
    Exchange rate and amount estimation for a trade.

    Attributes:
        from_amount: Input amount.
        to_amount: Projected output amount.
        rate: Exchange rate used for conversion.
    """

    model_config = ConfigDict(populate_by_name=True)

    from_amount: str = Field(alias="fromAmount")
    to_amount: str = Field(alias="toAmount")
    rate: str


class RangeRequest(BaseModel):
    """
    Request parameters for retrieving transaction ranges.

    Attributes:
        from_ticker: Source currency ticker.
        to_ticker: Target currency ticker.
        from_network: Source blockchain network.
        to_network: Target blockchain network.
    """

    model_config = ConfigDict(populate_by_name=True)

    from_ticker: str = Field(alias="fromTicker")
    to_ticker: str = Field(alias="toTicker")
    from_network: str = Field(alias="fromNetwork")
    to_network: str = Field(alias="toNetwork")


class Range(BaseModel):
    """
    Minimum and maximum transaction limits for a pair.

    Attributes:
        min_amount: Minimum allowed amount for exchange.
        max_amount: Maximum allowed amount for exchange (if restricted).
    """

    model_config = ConfigDict(populate_by_name=True)

    min_amount: str = Field(alias="minAmount")
    max_amount: Optional[str] = Field(alias="maxAmount", default=None)


class SwapRequest(BaseModel):
    """
    Request parameters for creating a new private swap.

    Attributes:
        from_ticker: Source currency ticker.
        to_ticker: Target currency ticker.
        amount: Transaction amount.
        address_to: Destination wallet address.
        from_network: Source blockchain network.
        to_network: Target blockchain network.
    """

    model_config = ConfigDict(populate_by_name=True)

    from_ticker: str = Field(alias="fromTicker")
    to_ticker: str = Field(alias="toTicker")
    amount: str
    address_to: str = Field(alias="addressTo")
    from_network: str = Field(alias="fromNetwork")
    to_network: str = Field(alias="toNetwork")


class SwapResponse(BaseModel):
    """
    Response details for a created private swap.

    Attributes:
        id: Unique tracking ID for the swap.
        status: Current status of the swap transaction.
        from_ticker: Source currency.
        to_ticker: Target currency.
        amount: Swap amount details.
        address_to: Destination wallet address.
        created_at: ISO timestamp of transaction creation.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    status: str
    from_ticker: str = Field(alias="fromTicker")
    to_ticker: str = Field(alias="toTicker")
    amount: str
    address_to: str = Field(alias="addressTo")
    created_at: Optional[str] = Field(alias="createdAt", default=None)


class SeedDestination(BaseModel):
    """
    Distribution target node for a private seed transaction.
    """

    model_config = ConfigDict(populate_by_name=True)

    address: str
    percentage: float


class SeedRequest(BaseModel):
    """
    Request parameters for creating a private seed distribution.

    Attributes:
        ticker: Currency ticker to distribute.
        total_amount: Total amount across all destination nodes.
        destinations: List of recipient nodes with percentage shares.
        network: Blockchain network for distribution.
    """

    model_config = ConfigDict(populate_by_name=True)

    ticker: str
    total_amount: str = Field(alias="totalAmount")
    destinations: List[SeedDestination]
    network: str


class SeedResponse(BaseModel):
    """
    Response details for a created seed distribution.

    Attributes:
        id: Unique tracking ID for the seed distribution.
        status: Current status of the distribution.
        total_amount: Total amount distributed across destination nodes.
        created_at: ISO timestamp of transaction creation.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    status: str
    total_amount: str = Field(alias="totalAmount")
    created_at: Optional[str] = Field(alias="createdAt", default=None)


class TransferRequest(BaseModel):
    """
    Request parameters for a single private proxy transfer.

    Attributes:
        ticker: Currency ticker to transfer.
        amount: Amount to send.
        address_to: Destination wallet address.
        network: Blockchain network for transfer.
    """

    model_config = ConfigDict(populate_by_name=True)

    ticker: str
    amount: str
    address_to: str = Field(alias="addressTo")
    network: str


class MultiTransferDestination(BaseModel):
    """
    Individual recipient for a multi-destination transfer.
    """

    model_config = ConfigDict(populate_by_name=True)

    address: str
    amount: str


class MultiTransferRequest(BaseModel):
    """
    Request parameters for a multi-destination private transfer.

    Attributes:
        ticker: Currency ticker to transfer.
        total_amount: Total cumulative amount for all recipients.
        destinations: List of recipients and their specific amounts.
        network: Blockchain network for transfer.
    """

    model_config = ConfigDict(populate_by_name=True)

    ticker: str
    total_amount: str = Field(alias="totalAmount")
    destinations: List[MultiTransferDestination]
    network: str


class TransferResponse(BaseModel):
    """
    Response details for a private proxy transfer.

    Attributes:
        id: Unique tracking ID for the transfer.
        status: Current status of the transfer.
        tx_hash: Blockchain transaction hash (if available).
        created_at: ISO timestamp of transaction creation.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    status: str
    tx_hash: Optional[str] = Field(alias="txHash", default=None)
    created_at: Optional[str] = Field(alias="createdAt", default=None)


class TrackingResponse(BaseModel):
    """
    Comprehensive status details for any transaction type.

    Attributes:
        id: Tracking ID.
        status: Progress status (e.g., 'pending', 'completed').
        type: Transaction type ('swap', 'seed', or 'transfer').
        details: Additional context and payload related to the transaction.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    status: str
    type: str
    details: Optional[Dict[str, Any]] = None


class VolumeResponse(BaseModel):
    """
    Platform statistics for trade volume.

    Attributes:
        total_volume_usd: Total trading volume in USD.
    """

    model_config = ConfigDict(populate_by_name=True)

    total_volume_usd: float = Field(alias="totalVolumeUsd")
