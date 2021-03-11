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


# --------------Terminal scripts--------------
#export FLASK_APP=api.py		for windows set FLASK_APP=api.py
#export FLASK_ENV=development       !!FOR DEBUG MODE!!
#flask run -h localhost -p 8765 --cert=adhoc

# --------------Online Tutorials--------------
# https://medium.com/@karthikeyan.ranasthala/build-a-jwt-based-authentication-rest-api-with-flask-and-mysql-5dc6d3d1cb82



#@@@@@@@@@@@@@@@@@@@@@@-- Modules --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Some libraries might be useless (copied-pasted from online tutorials)
from flask import Flask, Blueprint, request, jsonify
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
    return salt.hex


#@@@@@@@@@@@@@@@@@@@@@@-- DB auxilary --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def db_write(query, params):
    cur = mysql.connection.cursor()
    try:
        cur.execute(query, params)
        mysql.connection.commit()
        cur.close()

        return True

    except MySQLdb._exceptions.IntegrityError:
        cursor.close()
        return False

#@@@@@@@@@@@@@@@@@@@@@@-- JWT --#############@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

JWT_SECRET_KEY="SomeRandomSecretPhrase"

def encode_auth_token(self, user_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, hours=4),
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


# Auxilary

def validate_user_input(input_type, **kwargs):
    if input_type == "authentication":
        if len(kwargs["username"]) <= 255 and len(kwargs["password"]) <= 255:
            return True
        else:
            return False

# Auxilary_end

authentication = Blueprint("authentication", __name__)

@authentication.route("/register", methods=["POST"])
def register_user():
    pass

@authentication.route("/login", methods=["POST"])
def login_user():
    pass




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
<p>Except this marvelous paragraph, which shows that everything is OK</p>'''


@app.route('/admin/healthcheck', methods=['GET'])
def healthcheck():
	try:
		db_write("SELECT * FROM user","")
		return jsonify(status="OK")
	except:
		return jsonify(status="failed")


#to avoid some problems with dependecies, but it  doesn't work
#from blueprint_auth import authentication
#app.register_blueprint(authentication, url_prefix="/api/auth")
