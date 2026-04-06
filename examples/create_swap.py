"""
Example: Create Private Swap
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This script walks through the process of initiating a private token swap,
including estimating the output amount before transaction creation.
It demonstrates the use of the synchronous client for a sequential
swap creation workflow.
"""

from veillabs import VeilLabsClient


def main():
    """
    Main entry point for the swap creation example.
    """
    # Initialize the synchronous client
    with VeilLabsClient() as client:
        print("--- Veil Labs SDK (Private Swap Example) ---")

        # 1. Define the Swap parameters
        params = {
            "from_ticker": "eth",
            "from_network": "mainnet",
            "to_ticker": "btc",
            "to_network": "mainnet",
            "amount": "0.1",
            "address_to": "bc1q7x7...",  # Destination BTC address
        }

        # 2. Estimate the swap first (recommended)
        estimate = client.market.get_estimate(**params)
        print(f"Estimated Output: {estimate.to_amount} BTC")
        print(f"Current Rate: {estimate.rate}")

        # 3. Create the Swap (Uncomment to execute)
        # try:
        #     # In a real application, you would pass the actual destination address
        #     swap = client.swap.create(**params)
        #     print(f"\nSwap Created Successfully!")
        #     print(f"Status: {swap.status}")
        #     print(f"Tracking ID: {swap.id}")
        # except Exception as e:
        #     print(f"\nFailed to create swap: {e}")


if __name__ == "__main__":
    main()
