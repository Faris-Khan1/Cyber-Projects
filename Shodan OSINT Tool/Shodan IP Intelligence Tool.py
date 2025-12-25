from shodan import Shodan
import json

API_KEY = input("Enter your Shodan API key: ")
TARGET_IP = input("Enter the public IP to scan: ")

api = Shodan(API_KEY)

class ShodanHostDetails:
    def print_host_details(self, ip_address):
        ipinfo = api.host(ip_address)
        print(json.dumps(ipinfo, indent=4))

class ShodanHostDetailsParser:
    def parse_host_details(self, ip_address):
        ipinfo = api.host(ip_address)
        json_data = json.loads(json.dumps(ipinfo))

        print("IP:", json_data.get("ip_str"))
        print("City:", json_data.get("city"))
        print("Latitude:", json_data.get("latitude"))
        print("Longitude:", json_data.get("longitude"))
        print("Country Name:", json_data.get("country_name"))

if __name__ == "__main__":
    shodan_details = ShodanHostDetails()
    shodan_details.print_host_details(TARGET_IP)

    parser = ShodanHostDetailsParser()
    parser.parse_host_details(TARGET_IP)

