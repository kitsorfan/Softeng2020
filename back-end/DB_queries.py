import os
import hashlib
import datetime


from flask_mysqldb import MySQL
import mysql.connector



def hash_password(password,salt):
    key-hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),salt, 100000)
    return key

def create_salt():
    salt = os.urandom(32)
    return salt
