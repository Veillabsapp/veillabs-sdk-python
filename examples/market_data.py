"""
Example: Market Intelligence
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This script shows how to access real-time market data from the
Veil Labs platform, such as supported currencies,
trading pairs, and current price estimates.
"""

from veillabs import VeilLabsClient, EstimateRequest


def main():
    """
    Main entry point for the market data retrieval example.
    """
    # 1. Initialize the client using context management
    with VeilLabsClient() as client:
        print("--- Veil Labs SDK (Market Data Example) ---")

        # 2. Get all supported currencies
        try:
            currencies = client.market.get_currencies()
            print(f"Total Supported Currencies: {len(currencies)}")

            # Print the first three currencies as examples
            for curr in currencies[:3]:
                print(f"- {curr.name} ({curr.ticker}) on {curr.network}")

        except Exception as e:
            print(f"Failed to fetch currencies: {e}")

        # 3. Get all pairs for a specific ticker and network
        ticker, network = "eth", "mainnet"
        try:
            pairs = client.market.get_pairs(ticker, network)
            print(f"\nPairs for {ticker.upper()} on {network}:")

            # Print reachable destinations for Ethereum
            for pair in pairs[:5]:
                print(f"-> {pair.to_ticker} ({pair.to_network})")

        except Exception as e:
            print(f"Failed to fetch pairs: {e}")

        # 4. Get a current exchange estimate using an explicit model
        try:
            estimate_req = EstimateRequest(
                ticker_from="eth",
                network_from="mainnet",
                ticker_to="usdc",
                network_to="mainnet",
                amount="2.5",
            )

            estimate = client.market.get_estimate(estimate_req)

            print(f"\nEstimate: 2.5 ETH -> {estimate.estimated_amount} USDC")
            print(f"Rate ID: {estimate.rate_id}")
            print(f"Trace ID: {estimate.trace_id}")

        except ValueError as e:
            print(f"\n❌ API Error during estimate: {e}")
        except Exception as e:
            print(f"\n❌ Failed to calculate estimate: {e}")


if __name__ == "__main__":
    main()
