"""
Example: Unified Usage (Asynchronous)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This script demonstrates how to work with multiple modules in a single
Veil Labs async client session, including market estimates,
proxy transfers, and transaction tracking.
"""

import asyncio
from veillabs import AsyncVeilLabsClient, SwapRequest


async def main():
    """
    Main entry point for the async SDK usage example.
    """
    async with AsyncVeilLabsClient() as client:
        print("--- Veil Labs SDK (Unified Async Usage) ---")

        # 1. Fetch available currencies asynchronously
        markets = await client.market.get_currencies()
        print(f"Registered Currencies: {len(markets)}")

        # 2. Get an exchange estimate using the Pydantic model
        # We define a SwapRequest and reuse its parameters for rate estimation
        try:
            swap_req = SwapRequest(
                ticker_from="eth",
                network_from="mainnet",
                ticker_to="usdt",
                network_to="mainnet",
                amount="1.0",
                address_to="0x123...",
            )

            # The get_estimate method accepts a dictionary or an EstimateRequest model
            estimate = await client.market.get_estimate(
                {
                    "ticker_from": swap_req.ticker_from,
                    "network_from": swap_req.network_from,
                    "ticker_to": swap_req.ticker_to,
                    "network_to": swap_req.network_to,
                    "amount": swap_req.amount,
                }
            )
            print(f"\nEstimate (1.0 ETH): {estimate.estimated_amount} USDT")
            print(f"Trace ID: {estimate.trace_id}")

            # 3. Create a swap asynchronously
            swap = await client.swap.create(swap_req)
            print(f"\n✅ Swap created with ID: {swap.id}")
            print(f"Status: {swap.status}")

        except ValueError as e:
            print(f"\n❌ API Error during async swap: {e}")
        except Exception as e:
            print(f"\n❌ Failed to execute async swap: {e}")


if __name__ == "__main__":
    asyncio.run(main())
