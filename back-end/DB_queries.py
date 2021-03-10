import os
import hashlib
import datetime


from flask_mysqldb import MySQL
import mysql.connector

#@@@@@@@@@@@@@@@@@@@@@@-- DB conection --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   we are using the default port 3306

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sqlpassword'
app.config['MYSQL_DB'] = 'project_e_lectra'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' #optional

mysql = MySQL(app)

def hash_password(password,salt):
    key-hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),salt, 100000)
    return key

def create_salt():
    salt = os.urandom(32)
    return salt
