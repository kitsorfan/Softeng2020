
from hashlib import pbkdf2_hmac
import requests
import os
import hashlib




#@@@@@@@@@@@@@@@@@@@@@@-- Password Hashing --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def generate_hash(plain_password, password_salt):
    password_hash = pbkdf2_hmac(
        "sha256",
        b"%b" % bytes(plain_password, "utf-8"),
        b"%b" % bytes(password_salt, "utf-8"),
        10000,
    )
    return password_hash.hex()

def generate_salt():
    salt = os.urandom(32)
    return salt.hex()
