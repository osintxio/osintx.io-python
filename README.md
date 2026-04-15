# osintx_ API Python Examples

Requires **Python 3.7+** and [`requests`](https://pypi.org/project/requests/).

## Setup

```bash
pip install requests
```

Set your API key:

```bash
export OSINTX_API_KEY="oix_XXXXXXXX_XXXXXXXXXXXXXXXX_XXXXXXXX"
```

## Run

```bash
python osintx.py
```

Uncomment the function calls at the bottom of the script to try different search types.

## Available Functions

| Function | Search Type | Description |
|---|---|---|
| `get_account_usage()` | — | Check plan, daily searches & limits |
| `search_username(query)` | `username` | Social + breach database lookup |
| `search_email(query)` | `email` | Breach database lookup |
| `search_ip(query)` | `ip` | Geolocation, ASN, open ports, FiveM cross-ref |
| `search_discord(query)` | `discord` | Leak DB + FiveM ban DB cross-reference |
| `search_fivem(query)` | `fivem` | FiveM ID / IP / name across ban DBs |
| `search_crypto(address)` | `crypto` | Wallet balance, TXs, mixer flags |
| `search_phone(query)` | `phone` | Carrier, country, breach hits |
| `search_breaches(query)` | `breaches` | Email / username breach search |
| `search_minecraft(query)` | `minecraft` | Username or UUID lookup |
| `search_bank(query)` | `bank` | BIN / IIN lookup (6–8 digits) |
| `search_password(query)` | `password` | Plaintext password in breach dumps |
| `search_ddg(query)` | `ddg` | DuckDuckGo web search |

## Docs

Full API documentation: [https://osintx.io/docs](https://osintx.io/docs)
