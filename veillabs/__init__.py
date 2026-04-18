"""
Veil Labs Python SDK
~~~~~~~~~~~~~~~~~~~

The official Python SDK for interacting with the Veil Labs privacy platform.
Provides both Synchronous and Asynchronous clients.

Example (Sync):
    >>> from veillabs import VeilLabsClient
    >>> with VeilLabsClient() as client:
    >>>     currencies = client.market.get_currencies()

Example (Async):
    >>> from veillabs import AsyncVeilLabsClient
    >>> async with AsyncVeilLabsClient() as client:
    >>>     currencies = await client.market.get_currencies()
"""

from .sync_client import VeilLabsClient
from .async_client import AsyncVeilLabsClient
from .models import (
    Currency,
    Pair,
    Estimate,
    Range,
    SwapResponse,
    SeedResponse,
    TrackingResponse,
    VolumeResponse,
    EstimateRequest,
    RangeRequest,
    SwapRequest,
    SeedRequest,
    SeedDestination,
)

__all__ = [
    "VeilLabsClient",
    "AsyncVeilLabsClient",
    "Currency",
    "Pair",
    "Estimate",
    "Range",
    "SwapResponse",
    "SeedResponse",
    "TrackingResponse",
    "VolumeResponse",
    "EstimateRequest",
    "RangeRequest",
    "SwapRequest",
    "SeedRequest",
    "SeedDestination",
]
