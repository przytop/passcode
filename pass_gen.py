import random
import string
from argon2 import PasswordHasher
from cryptography.fernet import Fernet


def generate_master_password():
    # Create master password
    master = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    print(f'Your MASTER PASSWORD is: {master}')
    print('Save it now. You will need it to log in!!!')
    print("If you lose it, you won't be able to access your passwords")
    print('MASTER PASSWORD cannot be restored')
    input("Press Enter when ready...")

    # Hash it with argon2id
    ph = PasswordHasher()
    key = ph.hash(master)  # argon2 key
    print('Generated hash of MASTER PASSWORD')
    return key


def pass_generator(length):
    # Password generator whit string and random modules
    letters = string.ascii_letters  # A-z
    numbers = string.digits  # 0-9
    symbols = string.punctuation  # !-?
    all = letters + numbers + symbols  # All in one constant
    return ''.join(random.sample(all, length))  # Generator code


def encrypt(key, data):
    # Encrypt password whit Fernet (symmetric encryption), secret key needed
    enc = key.encode('utf-8')  # Str to bytes, Fernet key must be 32 url-safe base64-encoded bytes
    enc_data = Fernet(enc).encrypt(data.encode())   # Fernet encrypt code
    return enc_data


def decrypt(key, data):
    # Decrypt password whit Fernet (symmetric encryption), secret key needed
    dec_data = Fernet(key).decrypt(data).decode()   # # Fernet decrypt code
    return dec_data
