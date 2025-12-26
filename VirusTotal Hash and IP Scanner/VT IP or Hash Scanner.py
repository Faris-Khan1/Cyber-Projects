import requests
import json

def check_hash(hash_value, api_key):
    url = f"https://www.virustotal.com/api/v3/files/{hash_value}"
    headers = {"x-apikey": api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        stats = result.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
        print("VirusTotal Report:")
        print(json.dumps(stats, indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")


def check_ip(ip_address, api_key):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip_address}"
    headers = {"x-apikey": api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        ipstats = result.get("data", {}).get("attributes", {}).get("last_analysis_stats", {})
        print("VirusTotal Report:")
        print(json.dumps(ipstats, indent=4))
    else:
        print(f"Error {response.status_code}: {response.text}")


if __name__ == "__main__":
    api_key = input("Enter your VirusTotal API key: ")
    user_input = input("Enter a file hash or an IP address to check: ")

    if "." in user_input:
        check_ip(user_input, api_key)
    else:
        check_hash(user_input, api_key)