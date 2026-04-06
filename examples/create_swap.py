"""
Example: Create Private Swap
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This script walks through the process of initiating a private token swap,
including estimating the output amount before transaction creation.
It demonstrates the use of the synchronous client for a sequential
swap creation workflow.
"""

from veillabs import VeilLabsClient, SwapRequest


def main():
    """
    Main entry point for the swap creation example.
    """
    # Initialize the synchronous client
    with VeilLabsClient() as client:
        print("--- Veil Labs SDK (Private Swap Example) ---")

        # 1. Define the Swap parameters using the Pydantic model
        # Note: We now use ticker_from, network_from, etc. to align with the API.
        params = SwapRequest(
            ticker_from="eth",
            network_from="mainnet",
            ticker_to="usdc",
            network_to="mainnet",
            amount="1.0",
            address_to="0x1234567890abcdef1234567890abcdef12345678",
        )

        try:
            # 2. Get an estimate first (recommended)
            # The client accepts the SwapRequest model here too for convenience
            estimate = client.market.get_estimate(
                {
                    "ticker_from": params.ticker_from,
                    "network_from": params.network_from,
                    "ticker_to": params.ticker_to,
                    "network_to": params.network_to,
                    "amount": params.amount,
                }
            )
            print(f"Estimated Output: {estimate.estimated_amount} USDC")
            print(f"Trace ID: {estimate.trace_id}")

            # 3. Create the Swap
            swap = client.swap.create(params)

            print("\n✅ Swap Created Successfully!")
            print(f"Transaction ID: {swap.id}")
            print(f"Deposit Address: {swap.address_from}")
            print(f"Status: {swap.status}")
            print(f"Amount To Receive: {swap.amount_to} {swap.ticker_to}")

        except ValueError as e:
            print(f"\n❌ API Error: {e}")
        except Exception as e:
            print(f"\n❌ error: {e}")


if __name__ == "__main__":
    main()
