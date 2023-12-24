import random
import string
import time

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Enter the length for your password: "))
password = generate_password(password_length)
time.sleep(1)
print("[+] Generating Password")
time.sleep(1)
print("New Password:", password)
print("-------------------------")
print("Written by PXRSoftware")