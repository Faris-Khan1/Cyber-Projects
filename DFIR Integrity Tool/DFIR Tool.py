import os
import hashlib
import csv
import psutil

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class Dfir:
    def generate_fingerprints(self) -> None:
        file_list = os.listdir()
        with open('checksums.csv', 'w', newline='', encoding='utf-8') as checksums:
            writer = csv.writer(checksums)
            for file_name in file_list:
                if file_name.endswith('.py'):
                    with open(file_name, 'r', encoding='utf-8') as file:
                        plain_text = file.read()
                        hashed_text = hashlib.sha256(plain_text.encode()).hexdigest()
                        print(f"{file_name} , {hashed_text}")
                        writer.writerow([file_name, hashed_text])
        print("\n--- Fingerprints generated and saved in checksums.csv ---\n")

    def compare_fingerprints(self) -> bool:
        mismatch_found = False
        file_list = os.listdir()

        with open('checksums.csv', 'r', encoding='utf-8') as checksums:
            reader = csv.reader(checksums)
            mydict = {rows[0]: rows[1] for rows in reader}

        for file_name in file_list:
            if file_name.endswith('.py'):
                with open(file_name, 'r', encoding='utf-8') as file:
                    plain_text = file.read()
                    hashed_text = hashlib.sha256(plain_text.encode()).hexdigest()
                    if mydict.get(file_name) == hashed_text:
                        print(file_name, ': OK')
                    else:
                        print(file_name, ': Mismatch detected!')
                        mismatch_found = True

        return mismatch_found

    def get_last_logins_not_current_user(self, authorised_user) -> bool:
        unauthorised_user_found = False
        current_users = psutil.users()

        for user in current_users:
            if user.name != authorised_user:
                print(f"Unauthorised user found: {user.name}")
                unauthorised_user_found = True
            else:
                print(f"{user.name} is an authorised user")

        return unauthorised_user_found


if __name__ == "__main__":
    dfir_tool = Dfir()
    dfir_tool.generate_fingerprints()

    if dfir_tool.compare_fingerprints():
        print("\n--- Fingerprint mismatch found ---\n")
    else:
        print("\n--- No fingerprint mismatch found ---\n")

    if dfir_tool.get_last_logins_not_current_user('Faris'):
        print("\n--- Unauthorized user found ---\n")
    else:
        print("\n--- No unauthorized user found ---\n")

