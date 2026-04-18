from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, ConfigDict


class Currency(BaseModel):
    """
    Representation of a cryptocurrency available on the platform.
    """

    model_config = ConfigDict(populate_by_name=True)

    ticker: str
    name: str
    network: str
    image: Optional[str] = None
    has_external_id: bool = Field(alias="hasExternalId", default=False)
    is_fiat: bool = Field(alias="isFiat", default=False)
    featured: bool = Field(default=False)
    is_default: bool = Field(alias="isDefault", default=False)


class Pair(BaseModel):
    """
    Available trade pair between two cryptocurrencies.
    """

    model_config = ConfigDict(populate_by_name=True)

    from_ticker: str = Field(alias="fromTicker")
    from_network: str = Field(alias="fromNetwork")
    to_ticker: str = Field(alias="toTicker")
    to_network: str = Field(alias="toNetwork")


class EstimateRequest(BaseModel):
    """
    Request parameters for an exchange estimate.
    """

    model_config = ConfigDict(populate_by_name=True)

    ticker_from: str = Field(alias="tickerFrom")
    network_from: str = Field(alias="networkFrom")
    ticker_to: str = Field(alias="tickerTo")
    network_to: str = Field(alias="networkTo")
    amount: str


class Estimate(BaseModel):
    """
    Exchange rate and amount estimation for a trade.
    """

    model_config = ConfigDict(populate_by_name=True)

    estimated_amount: str = Field(alias="estimatedAmount")
    rate_id: Optional[str] = Field(alias="rateId", default=None)
    valid_until: Optional[str] = Field(alias="validUntil", default=None)
    trace_id: str = Field(alias="traceId")


class RangeRequest(BaseModel):
    """
    Request parameters for retrieving transaction ranges.
    """

    model_config = ConfigDict(populate_by_name=True)

    ticker_from: str = Field(alias="tickerFrom")
    network_from: str = Field(alias="networkFrom")
    ticker_to: str = Field(alias="tickerTo")
    network_to: str = Field(alias="networkTo")


class Range(BaseModel):
    """
    Minimum and maximum transaction limits for a pair.
    """

    model_config = ConfigDict(populate_by_name=True)

    min_amount: str = Field(alias="minAmount")
    max_amount: Optional[str] = Field(alias="maxAmount", default=None)


class SwapRequest(BaseModel):
    """
    Request parameters for creating a new private swap.
    """

    model_config = ConfigDict(populate_by_name=True)

    ticker_from: str = Field(alias="tickerFrom")
    network_from: str = Field(alias="networkFrom")
    ticker_to: str = Field(alias="tickerTo")
    network_to: str = Field(alias="networkTo")
    amount: str
    address_to: str = Field(alias="addressTo")
    fixed: Optional[bool] = None


class SwapResponse(BaseModel):
    """
    Response details for a created private swap.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    order_id: str = Field(alias="orderId")
    address_from: str = Field(alias="addressFrom")
    amount_from: str = Field(alias="amountFrom")
    amount_to: str = Field(alias="amountTo")
    status: str
    ticker_from: str = Field(alias="tickerFrom")
    network_from: str = Field(alias="networkFrom")
    ticker_to: str = Field(alias="tickerTo")
    network_to: str = Field(alias="networkTo")
    address_to: str = Field(alias="addressTo")
    trace_id: Optional[str] = Field(alias="traceId", default=None)


class SeedDestination(BaseModel):
    """
    Distribution target node for a private seed transaction.
    """

    model_config = ConfigDict(populate_by_name=True)

    address: str
    percentage: float
    ticker: str
    network: str


class SeedRequest(BaseModel):
    """
    Request parameters for creating a private seed distribution.
    """

    model_config = ConfigDict(populate_by_name=True)

    ticker_from: str = Field(alias="tickerFrom")
    network_from: str = Field(alias="networkFrom")
    ticker_to: str = Field(alias="tickerTo")
    network_to: str = Field(alias="networkTo")
    amount: str
    destinations: List[SeedDestination]


class SeedResponse(BaseModel):
    """
    Response details for a created seed distribution.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    status: str
    amount_from: str = Field(alias="amountFrom")
    ticker_from: str = Field(alias="tickerFrom")
    address_from: str = Field(alias="addressFrom")
    destinations: List[Any]



class TrackingResponse(BaseModel):
    """
    Comprehensive status details for any transaction type.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    status: str
    type: str
    details: Optional[Dict[str, Any]] = None


class VolumeResponse(BaseModel):
    """
    Platform statistics for trade volume.
    """

    # Volume data in TypeScript shows snake_case
    total_volume: float
    total_volume_24h: float
    total_volume_7d: float
    total_volume_30d: float
    total_volume_90d: float
