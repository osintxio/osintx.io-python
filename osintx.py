import os
import json
import requests

BASE_URL = "https://api.osintx.io/v1"
API_KEY = os.getenv("OSINTX_API_KEY", "oix_XXXXXXXX_XXXXXXXXXXXXXXXX_XXXXXXXX")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

def print_response(label: str, resp: requests.Response) -> None:
    print(f"  {label}")
    print(f"  {resp.status_code}")
    try:
        print(json.dumps(resp.json(), indent=2))
    except Exception:
        print(resp.text)
    print()

def get_account_usage() -> dict:
    resp = requests.get(f"{BASE_URL}/account/usage", headers=HEADERS)
    print_response("Account Usage", resp)
    return resp.json()

def search_username(query: str) -> dict:
    resp = requests.post(
        f"{BASE_URL}/search",
        headers=HEADERS,
        json={"query": query, "type": "username"},
    )
    print_response(f"{query}", resp)
    return resp.json()

def search_email(query: str) -> dict:
    resp = requests.post(
        f"{BASE_URL}/search",
        headers=HEADERS,
        json={"query": query, "type": "email"},
    )
    print_response(f"{query}", resp)
    return resp.json()

def search_ip(query: str) -> dict:
    resp = requests.post(
        f"{BASE_URL}/search",
        headers=HEADERS,
        json={"query": query, "type": "ip"},
    )
    print_response(f"{query}", resp)
    return resp.json()

def search_discord(query: str) -> dict:
    resp = requests.post(
        f"{BASE_URL}/search",
        headers=HEADERS,
        json={"query": query, "type": "discord"},
    )
    print_response(f"{query}", resp)
    return resp.json()

def search_fivem(query: str) -> dict:
    resp = requests.post(
        f"{BASE_URL}/search",
        headers=HEADERS,
        json={"query": query, "type": "fivem"},
    )
    print_response(f"{query}", resp)
    return resp.json()

def search_crypto(wallet_address: str) -> dict:
    resp = requests.post(
        f"{BASE_URL}/search",
        headers=HEADERS,
        json={"query": wallet_address, "type": "crypto"},
    )
    print_response(f"{wallet_address}", resp)
    return resp.json()

def search_phone(query: str) -> dict:
    resp = requests.post(
        f"{BASE_URL}/search",
        headers=HEADERS,
        json={"query": query, "type": "phone"},
    )
    print_response(f"{query}", resp)
    return resp.json()

def search_breaches(query: str) -> dict:
    resp = requests.post(
        f"{BASE_URL}/search",
        headers=HEADERS,
        json={"query": query, "type": "breaches"},
    )
    print_response(f"{query}", resp)
    return resp.json()

def search_minecraft(query: str, subtype: str = "username") -> dict:
    resp = requests.post(
        f"{BASE_URL}/search",
        headers=HEADERS,
        json={"query": query, "type": "minecraft", "subtype": subtype},
    )
    print_response(f"({subtype}): {query}", resp)
    return resp.json()

def search_bank(query: str) -> dict:
    resp = requests.post(
        f"{BASE_URL}/search",
        headers=HEADERS,
        json={"query": query, "type": "bank"},
    )
    print_response(f"{query}", resp)
    return resp.json()

def search_password(query: str) -> dict:
    resp = requests.post(
        f"{BASE_URL}/search",
        headers=HEADERS,
        json={"query": query, "type": "password"},
    )
    print_response(f"{query}", resp)
    return resp.json()

def search_ddg(query: str) -> dict:
    resp = requests.post(
        f"{BASE_URL}/search",
        headers=HEADERS,
        json={"query": query, "type": "ddg"},
    )
    print_response(f"{query}", resp)
    return resp.json()

if __name__ == "__main__":
    get_account_usage()
    # search_username("test")
    # search_email("test@example.com")
    # search_ip("1.1.1.1")
    # search_discord("1234567890123456789")
    # search_fivem("1234567890123456789")
    # search_crypto("123456789")
    # search_phone("+49123456789")
    # search_breaches("test@example.com")
    # search_minecraft("test", subtype="username")
    # search_bank("453201")
    # search_password("test")
    # search_ddg("osintx")
