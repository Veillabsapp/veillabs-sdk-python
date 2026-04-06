"""
Example: Asynchronous Usage
~~~~~~~~~~~~~~~~~~~~~~~~~~

This script demonstrates how to use the `AsyncVeilLabsClient` to perform
concurrent API requests using Python's asyncio module. It showcases
initializing the client with an async context manager and using
asyncio.gather to fetch data efficiently.
"""

import asyncio
from veillabs import AsyncVeilLabsClient


async def main():
    """
    Main entry point for the asynchronous usage example.
    """
    # Initialize the asynchronous client
    async with AsyncVeilLabsClient() as client:
        print("--- Veil Labs SDK (Async) ---")

        # 1. Fetch currencies concurrently (feature of async)
        print("\nFetching market data...")
        currencies_task = client.market.get_currencies()
        stats_task = client.stats.get_volume()

        currencies, stats = await asyncio.gather(currencies_task, stats_task)

        print(f"Supported Currencies: {len(currencies)}")
        print(f"Sample Currency: {currencies[0].ticker} ({currencies[0].name})")
        print(f"\nTotal Platform Volume: ${stats.total_volume_usd:,.2f}")

        # 2. Get Trading Pairs (concurrently for top assets)
        print("\nFetching pairs for eth/mainnet...")
        pairs = await client.market.get_pairs("eth", "mainnet")
        print(f"Available Destinations: {len(pairs)}")
        for pair in pairs[:3]:
            print(f"  - {pair.to_ticker} on {pair.to_network}")


if __name__ == "__main__":
    asyncio.run(main())
