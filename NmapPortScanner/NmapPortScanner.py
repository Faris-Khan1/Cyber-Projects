import nmap

class NmapPortScanner: #using a class here similar to the recipe in the book
    def port_scan(self, host):
        """
        Scan a host and print open ports.
        """
        nm = nmap.PortScanner()
        
        print(f"Select scan type:")
        print(f"1. Will quick scan the top 100 ports.")
        print(f"2. Will scan tcp ports from 1 to 1000")
        print(f"3. Your custom port range(Could take longer)")
        choice = input(f"Enter 1, 2, or 3: ")

        if choice == "1":
            arguments = "-F"
        elif choice == "2":
            arguments = "-p 1-1000"
        elif choice == "3":
            port_range = input(f"Enter port range (like 22-50): ")
            arguments = "-p " + port_range
        else:
            print("Invalid choice, using top 100 ports.")
            arguments = "-F"

        print(f"Scanning...")
        nm.scan(hosts=host, arguments=arguments)

        # Loop through hosts and ports
        for host_name in nm.all_hosts():
            if 'tcp' in nm[host_name]:
                print(f"\nOpen ports for host {host_name}:")
                for port in nm[host_name]['tcp']:
                    state = nm[host_name]['tcp'][port]['state']
                    service = nm[host_name]['tcp'][port]['name']
                    if state == "open":
                        print(f"Port {port} is open, Service: {service}")
                    else:
                        print(f"Port {port} is {state}")

if __name__ == "__main__":
    print("Nmap Project")
    host = input("Enter target host IP: ")
    scanner = NmapPortScanner()
    scanner.port_scan(host)




