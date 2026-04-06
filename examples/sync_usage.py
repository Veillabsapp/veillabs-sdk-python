"""
Example: Unified Usage (Synchronous)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This script demonstrates how to work with multiple modules in a single
Veil Labs sync client session, including market estimates,
proxy transfers, and transaction tracking.
"""

from veillabs import VeilLabsClient, SwapRequest


def main():
    """
    Main entry point for the unified synchronous SDK example.
    """
    # 1. Initialize the client using context management
    with VeilLabsClient() as client:
        print("--- Veil Labs SDK (Unified Sync Usage) ---")

        # 2. Get available currencies
        # markets = client.market.get_currencies()
        # print(f"Registered Currencies: {len(markets)}")

        # 3. Create a swap
        try:
            swap_req = SwapRequest(
                ticker_from="eth",
                network_from="mainnet",
                ticker_to="usdt",
                network_to="mainnet",
                amount="0.5",
                address_to="0x123...",
            )
            swap = client.swap.create(swap_req)
            print(f"Swap created with ID: {swap.id}")

            # 4. Check status of any transaction ID
            # In a real scenario, you'd wait for funds to confirm
            # status = client.track(swap.id)
            # print(f"Transaction ID: {status.id} | Status: {status.status}")

        except ValueError as e:
            print(f"API Error during swap: {e}")
        except Exception as e:
            print(f"Failed to execute swap: {e}")

        # 5. Get platform statistics
        try:
            stats = client.stats.get_volume()
            print("\nPlatform Statistics:")
            print(f"Total Trade Volume: ${stats.total_volume:.2f}")
        except Exception as e:
            print(f"Failed to fetch stats: {e}")


if __name__ == "__main__":
    main()
