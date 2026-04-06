from typing import List, Dict, Any, Optional
from ..base import BaseSyncSubClient
from ..models import Currency, Pair, Estimate, Range

class MarketSubClient(BaseSyncSubClient):
    """
    Synchronous sub-client for market data operations.
    """
    def get_currencies(self) -> List[Currency]:
        """
        Retrieves all supported currencies on the Veil Labs platform.
        
        Returns:
            A list of Currency objects representing supported assets.
        """
        response = self.http_client.get(f"{self.base_url}/currencies")
        response.raise_for_status()
        return [Currency(**c) for c in response.json()]

    def get_pairs(self, ticker: str, net: str) -> List[Pair]:
        """
        Retrieves all available pairs for a specific source asset.
        
        Args:
            ticker: Source currency ticker (e.g., 'eth').
            net: Source blockchain network (e.g., 'mainnet').
            
        Returns:
            A list of Pair objects showing valid trade destinations.
        """
        response = self.http_client.get(f"{self.base_url}/pairs/{ticker}/{net}")
        response.raise_for_status()
        return [Pair(**p) for p in response.json()]

    def get_estimate(self, **params) -> Estimate:
        """
        Calculates the estimated output amount and current rate for a trade.
        """
        response = self.http_client.get(f"{self.base_url}/estimates", params=params)
        response.raise_for_status()
        return Estimate(**response.json())

    def get_ranges(self, **params) -> Range:
        """
        Retrieves min and max trade limits for a specific pair.
        """
        response = self.http_client.get(f"{self.base_url}/ranges", params=params)
        response.raise_for_status()
        return Range(**response.json())
