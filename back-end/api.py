# e-Lectra Project by The Charging Aces:
# ~Stelios Kandylakis
# ~Margarita   Oikonomakou
# ~Kitsos      Orfanopoulos
# ~Vasilis     Papalexis
# ~Georgia     Stamou
# ~Dido        Stoikou
# Softeng, ECE NTUA, 2021

# API code

# --------------Prerequisites-----------------
#sudo apt-get install python-dev default-libmysqlclient-dev libssl-dev
# pip install -r requirements.txt

#export FLASK_APP=api.py
#export FLASK_ENV=development       !!FOR DEBUG MODE!!
#flask run -h localhost -p 8765 --cert=adhoc



#@@@@@@@@@@@@@@@@@@@@@@-- Modules --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Some libraries might be useless (copied-pasted from online tutorials)
from flask import Flask, Blueprint, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import flask_restx
from flask_mysqldb import MySQL
import mysql.connector

import os
import hashlib
import datetime
import jwt


#@@@@@@@@@@@@@@@@@@@@@@-- Api Creation --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

app = Flask(__name__)

if __name__ == "__main__":
	app.run(debug=True)


#@@@@@@@@@@@@@@@@@@@@@@-- DB conection --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   we are using the default port 3306

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sqlpassword'
app.config['MYSQL_DB'] = 'project_e_lectra'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' #optional


mysql = MySQL(app)

#@@@@@@@@@@@@@@@@@@@@@@-- Password Hashing --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def hash_password(password,salt):
    key-hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),salt, 100000)
    return key

def create_salt():
    salt = os.urandom(32)
    return salt


#@@@@@@@@@@@@@@@@@@@@@@-- JWT --#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def encode_auth_token(self, user_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e




#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$--- API ENDPOINTS ----$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#---------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------


#@@@@@@@@@@@@@@@@@@@@@@-- DB Healhcheck --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   This is an auxilary endpoint that shows the user that the DB is connected
#   and works properly.

@app.route('/demo', methods=['GET'])
def home():
    return '''<h1>Nothing to see here</h1>
<p>Except this marvelous paragraph, shows that everything is OK</p>'''


@app.route('/admin/healthcheck', methods=['GET'])
def healthcheck():
	try:
		cur = mysql.connection.cursor()
		cur.execute("SELECT * FROM user")
		mysql.connection.commit()
		cur.close()
		return jsonify(status="OK")
	except:
		return jsonify(status="failed")
