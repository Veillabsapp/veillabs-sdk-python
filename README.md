# Veil Labs Python SDK

[![Official SDK](https://img.shields.io/badge/Veil%20Labs-Official%20SDK-blue)](https://veillabs.app)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/Veillabsapp/veillabs-sdk-python.git)

The official Python SDK for **Veil Labs**, a privacy-first platform providing anonymous swaps (Private Swap), multi-destination distributions (Private Seed), and secure proxy transfers across multiple blockchain networks.

---

## 🚀 Features

- **Private Swaps**: Securely exchange tokens with built-in privacy.
- **Private Seed Distribution**: Distribute assets to multiple destination addresses in a single privacy-preserving transaction.
- **Proxy Transfers**: Anonymize your transfers via secure proxy nodes.
- **Market Intelligence**: Real-time access to supported currencies, pairs, and price estimates.
- **Dual Support**: Native support for both **Synchronous** and **Asynchronous** (asyncio) workflows.
- **Type-Safe Models**: Fully powered by Pydantic for robust data validation and IDE autocompletion.

---

## 📦 Installation

Install the SDK using `pip`:

```bash
pip install veillabs-python-sdk
```

Or using `uv` (recommended for modern workflows):

```bash
uv add veillabs-python-sdk
```

---

## 🏃 Quick Start

### Synchronous Client

Ideal for scripts and quick automation tasks.

```python
from veillabs import VeilLabsClient

# Connect using the synchronous client
with VeilLabsClient() as client:
    # 1. Fetch available currencies
    currencies = client.market.get_currencies()
    print(f"Supported Currencies: {len(currencies)}")

    # 2. Get an exchange estimate
    estimate = client.market.get_estimate(
        fromTicker="eth",
        toTicker="usdc",
        fromAmount="1.0",
        fromNetwork="mainnet",
        toNetwork="mainnet"
    )
    print(f"1 ETH = {estimate.to_amount} USDC")
```

### Asynchronous Client

Recommended for high-concurrency environments like web services (FastAPI, Django, etc.).

```python
import asyncio
from veillabs import AsyncVeilLabsClient

async def main():
    async with AsyncVeilLabsClient() as client:
        # Fetch platform stats
        stats = await client.stats.get_volume()
        print(f"Total Platform Volume: ${stats.total_volume_usd:,.2f}")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🛠 Detailed Usage

### 1. Market Data (`client.market`)

Access real-time data about the platform's supported assets and trading pairs.

- `get_currencies()`: Retrieve list of all supported cryptocurrencies.
- `get_pairs(ticker, net)`: Get valid trading destinations for a specific asset.
- `get_estimate(**params)`: Calculate real-time exchange rates and output values.
- `get_ranges(**params)`: Determine minimum and maximum transaction limits.

### 2. Private Swaps (`client.swap`)

Initiate anonymous cross-chain or same-chain token exchanges.

```python
swap = client.swap.create(
    fromTicker="eth",
    toTicker="btc",
    amount="0.5",
    addressTo="1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2",
    fromNetwork="mainnet",
    toNetwork="mainnet"
)
print(f"Swap Created! Tracking ID: {swap.id}")
```

### 3. Private Seed Distribution (`client.seed`)

Distribute a fixed amount of cryptocurrency to multiple recipient addresses.

```python
seed = client.seed.create(
    ticker="usdt",
    totalAmount="1000",
    destinations=[
        {"address": "0x123...", "percentage": 50},
        {"address": "0x456...", "percentage": 50}
    ],
    network="bsc"
)
```

### 4. Proxy Transfers (`client.transfer`)

Move funds securely through the Veil Labs proxy nodes to obfuscate the transaction path.

- `client.transfer.single(**params)`: Secure transfer to one recipient.
- `client.transfer.multi(**params)`: Secure transfer to multiple recipients.

### 5. Unified Transaction Tracking (`client.track`)

Maintain full visibility of your transaction progress using the unified `track` method.

```python
status = client.track("TRANSACTION_ID")
print(f"Current Status: {status.status}") # e.g., 'pending', 'completed'
```

---

## 📊 Models & Data Structures

Every response is returned as a **Pydantic** model, providing built-in validation and type hinting.

| Model | Purpose |
| :--- | :--- |
| `Currency` | Details about an asset (ticker, name, network, logo). |
| `Pair` | Details about available trading pairs. |
| `Estimate` | Rate and amount calculation results. |
| `SwapResponse` | Success response and metadata for new swaps. |
| `TrackingResponse` | Universal status check result. |

---

## 🛡 Network & Error Handling

The SDK utilizes `httpx` and raises standard status exceptions for API errors.

```python
import httpx
from veillabs import VeilLabsClient

try:
    with VeilLabsClient() as client:
        result = client.market.get_estimate(fromTicker="eth", ...)
except httpx.HTTPStatusError as e:
    print(f"API returned error: {e.response.status_code}")
except Exception as e:
    print(f"Connection error: {e}")
```

---

## 🔗 Links

- **Official Website**: [veillabs.app](https://veillabs.app)
- **GitHub Repository**: [Veillabsapp/veillabs-sdk-python](https://github.com/Veillabsapp/veillabs-sdk-python)
- **PyPI Package**: [veillabs-python-sdk](https://pypi.org/project/veillabs-python-sdk/)

---

## 📄 License

This SDK is open-source software licensed under the **MIT License**. See [LICENSE](LICENSE) for the full text.

---

<p align="center">
  <b>Developed with privacy at its core by Veil Labs.</b>
</p>
