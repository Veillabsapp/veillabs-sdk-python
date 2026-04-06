"""
Example: Synchronous Usage
~~~~~~~~~~~~~~~~~~~~~~~~

This script demonstrates how to use the synchronous `VeilLabsClient` to interact
with the Veil Labs API. It covers initializing the client, fetching supported
currencies, and retrieving platform statistics.
"""

from veillabs import VeilLabsClient


def main():
    """
    Main entry point for the synchronous usage example.
    """
    # Initialize the synchronous client
    # You can specify a custom base_url if needed
    with VeilLabsClient() as client:
        print("--- Veil Labs SDK (Sync) ---")

        # 1. Get supported currencies
        print("\nFetching currencies...")
        currencies = client.market.get_currencies()
        featured = [c.ticker for c in currencies if c.is_featured]
        print(f"Supported Currencies: {len(currencies)}")
        print(f"Featured: {', '.join(featured)}")

        # 2. Get platform volume
        stats = client.stats.get_volume()
        print(f"\nTotal Platform Volume: ${stats.total_volume_usd:,.2f}")

        # 3. Track a transaction (example ID)
        # try:
        #     status = client.track("0x123...")
        #     print(f"\nTransaction Type: {status.type}")
        #     print(f"Status: {status.status}")
        # except Exception as e:
        #     print(f"\nCould not track: {e}")


if __name__ == "__main__":
    main()
