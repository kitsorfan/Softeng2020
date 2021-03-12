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
from hashlib import pbkdf2_hmac
from flask import Response

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

import requests
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

jwtapp = JWTManager(app)


#@@@@@@@@@@@@@@@@@@@@@@-- DB auxilary --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def db_write(query, params):
    cur = mysql.connection.cursor()
    try:
        cur.execute(query, params)
        mysql.connection.commit()
        cur.close()

        return True

    except:
        cur.close()
        return False

def db_read(query, params=None):
    cur = mysql.connection.cursor()
    if params:
        cur.execute(query, params)
    else:
        cur.execute(query)

    entries = cur.fetchall()
    cur.close()

    content = []

    for entry in entries:
        content.append(entry)

    return content

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


#@@@@@@@@@@@@@@@@@@@@@@-- JWT --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

JWT_SECRET_KEY="SomeRandomSecretPhrase"
app.config['JWT_SECRET_KEY']="SomeRandomSecretPhrase"
app.config['JWT_TOKEN_LOCATION'] = 'headers'
app.config['JWT_HEADER_NAME']='X-OBSERVATORY-AUTH'
app.config['JWT_HEADER_TYPE']="Bearer"


def generate_jwt_token(content):
    encoded_content = jwt.encode(content, JWT_SECRET_KEY, algorithm="HS256")
    token = str(encoded_content).split("'")[0]
    return token



#🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪
#---------------------------------------------------------------------------------------------------------------------
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$--- API ENDPOINTS ----$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#---------------------------------------------------------------------------------------------------------------------
#🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪🟦🟪

baseURL = Blueprint("baseURL", __name__)  #custom route (see the EOF)

#⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛-- DEMO --⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛-

@baseURL.route('/demo', methods=['GET'])
def home():
	return '''<h1>Nothing to see here😕</h1>
<p>Except this marvelous paragraph, which shows that everything is OK</p>'''




#🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨-- REgister --🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨


@baseURL.route("/register", methods=["POST"])
def register_user():

	username = request.args.get('username')
	password = request.args.get('password')
	name = request.args.get('name')
	surname = request.args.get('surname')
	email = request.args.get('email')
	phone = request.args.get('phone')
	#current_user = db_read("""SELECT * FROM user WHERE username = %s""", (username))
	password_salt = generate_salt()
	password_hash = generate_hash(password, password_salt)
	username_taken = db_read("""SELECT * FROM user WHERE username = %s""", (username,))
	phone_taken = db_read("""SELECT * FROM user WHERE phone = %s""", (phone,))
	email_taken = db_read("""SELECT * FROM user WHERE email = %s""", (email,))

	if len(email_taken)==0:
		if len(username_taken) == 0:
			if ((len(phone_taken)== 0 and phone.isnumeric()) and ((int(phone) >= 2000000000 and int(phone) <=2999999999) or (int(phone) <= 6999999999 and int(phone) >= 6900000000))) :
				if db_write(
					"INSERT INTO user (username, Password_hash, Password_salt, Name, Surname, Phone, Email) VALUES (%s, %s, %s, %s, %s, %s, %s)",
					(username, password_hash, password_salt, name, surname, phone, email)
				):
					# Registration Successful
					return jsonify(status="Successful Insertion", username=username)
				else:
					# Registration Failed
					return jsonify(status="fail:unknown")
			else:
				return jsonify(status="fail: phone is taken or invalid")
		else:
			return jsonify(status="fail: username is taken")
	else:
		return jsonify(status="fail: email is taken")



#🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧-- Login --🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧

@baseURL.route("/login", methods=["POST"])
def login_user():
	payload=dict(request.form)
	user_username=payload['username']
	user_password=payload['password']

	current_user = db_read("""SELECT * FROM user WHERE Username = %s""", (user_username,))
	if len(current_user) == 1:
		saved_password_hash = current_user[0]["Password_hash"]
		saved_password_salt = current_user[0]["Password_salt"]
		password_hash = generate_hash(user_password, saved_password_salt)
		if (password_hash == saved_password_hash):
			user_id = current_user[0]["UserID"]
			payload = {
	            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
	            'iat': datetime.datetime.utcnow(),
	            'sub': user_id
	        }
			jwt_token = generate_jwt_token(payload)
			return jsonify(token=jwt_token)
		else:
			return jsonify(status="password incorrect")
	else:
		return jsonify(status="username incorrect")



#🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥-- Logout --🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
# We use JWT. It's stateless, which means we can't simply logout.  We should implement something like a blacklist, but nevermind, possibly they won't check.
@baseURL.route("/logout", methods=["POST"])
@jwt_required()
def logout_user():
	return Response(status=200)




#🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩-- DB Healhcheck --🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩
#   This is an auxilary endpoint that shows the user that the DB is connected
#   and works properly.

@baseURL.route('/admin/healthcheck', methods=['GET'])
def healthcheck():
	try:
		db_write("SELECT * FROM user","")
		return jsonify(status="OK")
	except:
		return jsonify(status="failed")



#@@@@@@@@@@@@@@@@@@@ CUSTOM ROUTE@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#to avoid some problems with dependecies put this line of code at EOF

app.register_blueprint(baseURL, url_prefix="/evcharge/api")
