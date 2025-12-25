import whois as ws
import json

class WhoisInfo:
    def get_whois_info(self, host):
        whois_info = ws.whois(host)
        json_output = json.dumps(whois_info, default=str, indent=4)
        print(json_output)

if __name__ == "__main__":
    domain = input("Enter a domain: ")
    whois_checker = WhoisInfo()
    whois_checker.get_whois_info(domain)

