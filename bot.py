import requests

url = "https://api.hyperliquid.xyz/info"

payload = {
    "type": "metaAndAssetCtxs",
    "dex": "xyz"
}

response = requests.post(url, json=payload, timeout=20)

print("Status:", response.status_code)
print("Data:")
print(response.json())
