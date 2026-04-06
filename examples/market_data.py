"""
Example: Detailed Market Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This script shows how to access market-related information like currencies,
trading pairs, exchange rate estimates, and transaction limits.
It demonstrates the use of the synchronous client for reading market configuration.
"""

from veillabs import VeilLabsClient


def main():
    """
    Main entry point for the market data example.
    """
    # Initialize the synchronous client
    with VeilLabsClient() as client:
        print("--- Veil Labs SDK (Market Data Detailed) ---")

        # 1. Get Currencies
        print("\nFetching currencies...")
        currencies = client.market.get_currencies()
        featured = [c.ticker for c in currencies if c.is_featured]
        print(f"Supported Assets: {len(currencies)}")
        print(f"Featured: {', '.join(featured)}")

        # 2. Get Pairs for ETH on Mainnet
        ticker = "eth"
        net = "mainnet"
        print(f"\nFetching pairs for {ticker} on {net}...")
        pairs = client.market.get_pairs(ticker, net)
        print(f"Available Destinations: {len(pairs)}")
        for pair in pairs[:5]:
            print(f"  - {pair.to_ticker} on {pair.to_network}")

        # 3. Get Estimate for a Swap
        print(f"\nEstimating swap: 0.1 {ticker}/{net} to btc/mainnet...")
        params = {
            "from_ticker": ticker,
            "from_network": net,
            "to_ticker": "btc",
            "to_network": "mainnet",
            "amount": "0.1",
        }
        try:
            estimate = client.market.get_estimate(**params)
            print(f"Estimated: {estimate.to_amount} btc")
            print(f"Rate: {estimate.rate}")
        except Exception as e:
            print(f"Could not fetch estimate: {e}")

        # 4. Get ranges for the same swap
        print(f"\nFetching limits for {ticker} -> btc...")
        try:
            ranges = client.market.get_ranges(**params)
            print(f"Min: {ranges.min_amount} {ticker}")
            if ranges.max_amount:
                print(f"Max: {ranges.max_amount} {ticker}")
            else:
                print("Max: Unlimited")
        except Exception as e:
            print(f"Could not fetch ranges: {e}")


if __name__ == "__main__":
    main()
