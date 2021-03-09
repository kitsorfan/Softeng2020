# e-Lectra Project by The Charging Aces:
# ~Stelios Kandylakis
# ~ Margarita  Oikonomakou
# ~Kitsos     Orfanopoulos
# ~Vasilis    Papalexis
# ~Georgia    Stamou
# ~Dido       Stoikou
# Softeng, ECE NTUA, 2021


# Auxilary Code for sql queries. API calls functions from this file.

# --------------Prerequisites-----------------
# pip3 install mysql-connector-python-rf
# pip3 install mysql-connector-python

#@@@@@@@@@@@@@@@@@@@@@@-- Libraries --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import hashlib
import os
import mysql.connector
import datetime

mydb = mysql.connector.connect(
    user="root",
    password="sqlpassword",
    database="project_e_lectra",
    host="127.0.0.1",
    port="3306",
    auth_plugin='mysql_native_password',
    use_pure='True'
)
pointer = mydb.cursor()  # to iterate to DB

#@@@@@@@@@@@@@@@@@@@@@@-- Password Hashing --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def hash_password(password, salt):
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return key

def create_salt():  #alataki xD
    salt = os.urandom(32)
    return salt
