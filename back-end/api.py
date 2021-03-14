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
#set FLASK_DEBUG=1

# --------------Online Tutorials--------------
# https://medium.com/@karthikeyan.ranasthala/build-a-jwt-based-authentication-rest-api-with-flask-and-mysql-5dc6d3d1cb82


#-------- Other Comments ---------------------------
# We are prone to SQL injections... TOFO: fix this threat


#@@@@@@@@@@@@@@@@@@@@@@-- Modules --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Some libraries might be useless (copied-pasted from online tutorials)
from flask import Flask, Blueprint, request, jsonify, g
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import flask_restx
from flask_mysqldb import MySQL
import mysql.connector
from hashlib import pbkdf2_hmac
from flask import Response
from datetime import datetime

import decimal

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager, get_jwt

import json
import csv


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




#🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨-- Register --🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨


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
	username_taken = db_read("""SELECT * FROM User WHERE username = %s""", (username,))
	phone_taken = db_read("""SELECT * FROM User WHERE phone = %s""", (phone,))
	email_taken = db_read("""SELECT * FROM User WHERE email = %s""", (email,))

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

	current_user = db_read("""SELECT * FROM User WHERE Username = %s""", (user_username,))
	if len(current_user) == 1:
		saved_password_hash = current_user[0]["Password_hash"]
		saved_password_salt = current_user[0]["Password_salt"]
		password_hash = generate_hash(user_password, saved_password_salt)
		if (password_hash == saved_password_hash):
			user_id = current_user[0]["UserID"]
			payload = {
	            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
	            'iat': datetime.datetime.utcnow(),
	            'sub': str(user_id)
	        }
			jwt_token = generate_jwt_token(payload)
			return jsonify(token=jwt_token)
		else:
			return jsonify(status="password incorrect")
	else:
		return jsonify(status="username incorrect")



#🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪-- Logout --🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
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



#🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥-- resetsession --🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥
#   This is not a  toy! If you use this command all the sessions at the DB are dropped
# 	and the default admin is resetting to amdin-petrol4ever

@baseURL.route('/admin/resetsessions', methods=['POST'])
def resetsessions():
	if not(db_write("""TRUNCATE TABLE session""","")):	#reset the sessions
		return  jsonify(status="failed")
	else:
		username = 'admin'
		password = "petrol4ever"
		password_salt = generate_salt()
		password_hash = generate_hash(password, password_salt)

		admin_exists = db_read("""SELECT * FROM User WHERE Username = %s""", (username,))
		if len(admin_exists) == 0:	#doesn't exist
			if db_write(
				"INSERT INTO user (username, Password_hash, Password_salt, IsAdmin) VALUES (%s, %s, %s, 1)",
				(username, password_hash, password_salt)
			):
				return jsonify(status="OK")
			else:
				return jsonify(status="fail")
		else:
			if (db_write("UPDATE User SET Password_hash = %s , Password_salt = %s  WHERE username = 'admin'",(password_hash, password_salt))):
				return jsonify(status="ok")
			else:
				return jsonify(status="fail")


#🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦-- usermod --🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦
#   Only admin
#	This is a method to add a new user, or update their password

@baseURL.route('/admin/usermod/<username>/<password>', methods=['POST'])
@jwt_required()
def usermod(username, password):

	#parse the arguments from the URL and create the salt
	g.username = username
	g.password = password
	password_salt = generate_salt()
	password_hash = generate_hash(password, password_salt)

	#firstly we have to check whether we have an admin OR AN IMPOSTOR!
	payload=get_jwt()	#get the whole jwt token
	id=payload["sub"]	#get the id of that token, that's the id of the user

	current_user = db_read("""SELECT * FROM User WHERE userID = %s""", (id,))
	is_admin = current_user[0]["IsAdmin"]

	if (is_admin==1):
		username_taken = db_read("""SELECT * FROM User WHERE username = %s""", (username,))
		if len(username_taken) == 0:
			if db_write(
				"INSERT INTO user (username, Password_hash, Password_salt) VALUES (%s, %s, %s)",
				(username, password_hash, password_salt)
			):
				return jsonify(status="successful Insertion")
			else:
				return Response(status=402)
		else:
			if (db_write("UPDATE user SET Password_hash = %s , Password_salt = %s  WHERE username = %s",(password_hash, password_salt, username))):
				return jsonify(status="successful update")
			else:
				return Response(status=402)
	else:
		return Response(status=401)



#🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪-- users --🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪🟪
#   Only admin
#	This is a method to see the full details of a users

@baseURL.route('/admin/users/<username>', methods=['GET'])
@jwt_required()
def users(username):

	g.username = username

	#firstly we have to check whether we have an admin OR AN IMPOSTOR!
	payload=get_jwt()	#get the whole jwt token
	id=payload["sub"]	#get the id of that token, that's the id of the user

	current_user = db_read("""SELECT * FROM user WHERE userID = %s""", (id,))
	is_admin = current_user[0]["IsAdmin"]

	if (is_admin==1):
		this_user = db_read("""SELECT * FROM User WHERE username = %s""", (username,))
		userID = this_user[0]["UserID"]
		email = this_user[0]["email"]
		Name = this_user[0]["Name"]
		Surname = this_user[0]["Surname"]
		BonusPoints = this_user[0]["BonusPoints"]
		Phone = this_user[0]["Phone"]
		ΙsAdmin = this_user[0]["IsAdmin"]
		admin = "no"
		if (ΙsAdmin == 1):
			admin = "yes"
		return jsonify(userID=userID,email=email,name=Name,surname=Surname,BonusPoints=BonusPoints,phone=Phone,admin=admin)
	else:
		return jsonify(status="fail: no admin permissions")



#🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨-- sessionupd --🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
#   Only admin
#	This is a method that emulates the way real session data are added to the DB

#@baseURL.route('/admin/system/sessionupd', methods=['GET'])
#@jwt_required()
#def sessionupd():

#🟩🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟩-- 2a SessionsPerPoint --🟩🟧🟧🟧🟧🟧🟧🟧🟧🟧🟧🟩

@baseURL.route('/SessionsPerPoint/<pointID>/<yyyymmdd_from>/<yyyymmdd_to>', methods=['GET'])
@jwt_required()
def SessionsPerPoint(pointID, yyyymmdd_from, yyyymmdd_to):
	#parse the args
	g.pointID = pointID
	g.yyyymmdd_from = yyyymmdd_from
	g.yyyymmdd_to = yyyymmdd_to

	format = request.args.get('format', default=None)
	if (format == None): format = 'json'


	#check point ID
	if (not(pointID.isdigit()) or not(yyyymmdd_from.isdigit()) or not(yyyymmdd_to.isdigit())):
		return Response(status=400)

	point_exists = db_read("""SELECT * FROM ChargingPoint WHERE PointID = %s""", (int(pointID),))

	if (len(point_exists) == 0): #no such a point
		return Response(status=400)

	operatorlist = db_read("""SELECT st.Operator FROM ChargingPoint AS c INNER JOIN station AS st USING (StationID) WHERE c.PointID = %s """, (pointID,))
	operator=operatorlist[0]

	#check year

	start_year = yyyymmdd_from[0] + yyyymmdd_from[1] + yyyymmdd_from[2] + yyyymmdd_from[3]
	finish_year = yyyymmdd_to[0] + yyyymmdd_to[1] + yyyymmdd_to[2] + yyyymmdd_to[3]

	current_year = datetime.datetime.now().year

	if ((int(finish_year)>int(current_year)) or (int(finish_year)<int(start_year))):
		return Response(status=400)

	#check month
	start_month = yyyymmdd_from[4] + yyyymmdd_from[5]
	finish_month = yyyymmdd_to[4] + yyyymmdd_to[5]

	if ((int(start_month)>13) or (int(finish_month)>13) or (int(start_month)<1) or (int(finish_month)<0) ):
		return Response(status=400)

	#check day
	start_day = yyyymmdd_from[6] + yyyymmdd_from[7]
	finish_day = yyyymmdd_to[6] + yyyymmdd_to[7]

	if ((int(start_day)>31) or (int(finish_day)>31) or (int(start_day)<1) or (int(finish_day)<0)):
		return Response(status=400)

	start_date=start_year+"-"+start_month+"-"+start_day
	finish_date=finish_year+"-"+finish_month+"-"+finish_day

	current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	db_write("""SET @rank=0;""",())
	requested_sessions = db_read(""" SELECT @rank:=@rank+1 AS SessionIndex, SessionID, StartedOn, FinishedOn, Protocol, FORMAT(EnergyDelivered,2) AS EnergyDelivered, PaymentType, Ve.Type FROM session INNER JOIN vehicle AS Ve USING (VehicleID) WHERE pointID=%s AND DATE(FinishedON) BETWEEN %s AND %s""",(int(pointID), start_date, finish_date))

	NumberOfChargingSessions = len(requested_sessions)


	#special date format

	for i in range(len(requested_sessions)):
		requested_sessions[i]["StartedOn"]=requested_sessions[i]["StartedOn"].strftime("%Y-%m-%d %H:%M:%S")
		requested_sessions[i]["FinishedOn"]=requested_sessions[i]["FinishedOn"].strftime("%Y-%m-%d %H:%M:%S")


	if (format == 'json'):
		return jsonify(Point=pointID, PointOperator=operator['Operator'], RequestTimestamp=current_timestamp, PeriodFrom=start_date, PeriodTo=finish_date, NumberOfChargingSessions=NumberOfChargingSessions, ChargingSessionsList=requested_sessions)
	elif (format == 'csv'):
	    #-- first row must have the names of the columns (attibutes of the entity)
		csv=""
		csv=csv+"Point,PointOperator,RequestTimestamp,PeriodFrom,PeriodTo,NumberOfChargingSessions,SessionIndex,SessionID,StartedOn,FinishedOn,Protocol,EnergyDelivered,Payment,VehicleType\n"
		i=0
		while i<NumberOfChargingSessions:
			csv=csv+str(pointID)+","+operator['Operator']+","+str(current_timestamp)+","+str(start_date)+","+ str(finish_date)+","+ str(NumberOfChargingSessions)+","+str(requested_sessions[i]["SessionIndex"])+","+str(requested_sessions[i]["SessionID"])+","+str(requested_sessions[i]["StartedOn"])+","+str(requested_sessions[i]["FinishedOn"])+","+requested_sessions[i]["Protocol"]+","+str(requested_sessions[i]["EnergyDelivered"])+","+requested_sessions[i]["PaymentType"]+","+requested_sessions[i]["Type"]+"\n"
			i=i+1
		return Response(csv, mimetype='text/csv')
	else:
		return Response(status=400)



#🟩🟩🟧🟧🟧🟧🟧🟧🟧🟧🟩🟩-- 2b SessionsPerStation --🟩🟩🟧🟧🟧🟧🟧🟧🟧🟧🟩🟩

@baseURL.route('/SessionsPerStation/<stationID>/<yyyymmdd_from>/<yyyymmdd_to>', methods=['GET'])
@jwt_required()
def SessionsPerStation(stationID, yyyymmdd_from, yyyymmdd_to):
	#parse the args
	g.stationID = stationID
	g.yyyymmdd_from = yyyymmdd_from
	g.yyyymmdd_to = yyyymmdd_to

	format = request.args.get('format', default=None)
	if (format == None): format = 'json'

	#check point ID
	if (not(stationID.isdigit()) or not(yyyymmdd_from.isdigit()) or not(yyyymmdd_to.isdigit())):
		return Response(status=400)

	station_exists = db_read("""SELECT * FROM Station WHERE StationID = %s""", (int(stationID),))

	if (len(station_exists) == 0): #no such a point
		return Response(status=400)

	operatorlist = db_read("""SELECT Operator FROM Station WHERE stationID = %s """, (int(stationID),))
	operator=operatorlist[0]

	#check year

	start_year = yyyymmdd_from[0] + yyyymmdd_from[1] + yyyymmdd_from[2] + yyyymmdd_from[3]
	finish_year = yyyymmdd_to[0] + yyyymmdd_to[1] + yyyymmdd_to[2] + yyyymmdd_to[3]

	current_year = datetime.datetime.now().year

	if ((int(finish_year)>int(current_year)) or (int(finish_year)<int(start_year))):
		return Response(status=400)

	#check month
	start_month = yyyymmdd_from[4] + yyyymmdd_from[5]
	finish_month = yyyymmdd_to[4] + yyyymmdd_to[5]

	if ((int(start_month)>13) or (int(finish_month)>13) or (int(start_month)<1) or (int(finish_month)<0) ):
		return Response(status=400)

	#check day
	start_day = yyyymmdd_from[6] + yyyymmdd_from[7]
	finish_day = yyyymmdd_to[6] + yyyymmdd_to[7]

	if ((int(start_day)>31) or (int(finish_day)>31) or (int(start_day)<1) or (int(finish_day)<0)):
		return Response(status=400)

	start_date=start_year+"-"+start_month+"-"+start_day
	finish_date=finish_year+"-"+finish_month+"-"+finish_day

	current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


	TotalEnergyDeliveredlist = db_read("""SELECT FORMAT(SUM(ses.EnergyDelivered),2) AS TotalEnergyDelivered FROM  session ses INNER JOIN ChargingPoint ch USING(PointID) WHERE ch.StationID=%s AND DATE(FinishedON) BETWEEN %s AND %s""",(stationID, start_date, finish_date))
	TotalEnergyDelivered=TotalEnergyDeliveredlist[0]

	ActivePointsList = db_read("""SELECT PointID, Count(PointID) AS PointSessions, FORMAT(SUM(ses.EnergyDelivered),2) AS EnergyDelivered FROM  session ses INNER JOIN ChargingPoint ch USING(PointID) WHERE ch.StationID=%s AND EnergyDelivered>0 AND DATE(FinishedON) BETWEEN %s AND %s  GROUP BY PointID""",(stationID, start_date, finish_date))
	NumberofActivePoints = len(ActivePointsList)



	if (format == 'json'):
		return jsonify(StationID=stationID, Operator=operator['Operator'], RequestTimestamp=current_timestamp, PeriodFrom=start_date, PeriodTo=finish_date, TotalEnergyDelivered=TotalEnergyDelivered['TotalEnergyDelivered'], NumberofActivePoints=NumberofActivePoints, SessionSummaryList=ActivePointsList)

	elif (format == 'csv'):
	    #-- first row must have the names of the columns (attibutes of the entity)
		csv=""
		csv=csv+"StationID,Operator,RequestTimestamp,PeriodFrom,PeriodTo,TotalEnergyDelivered,NumberOfChargingSessions,NumberOfActivePoints,PointID,PointSessions,EnergyDelivered\n"
		i=0
		while i<NumberofActivePoints:
			csv=csv+str(stationID)+","+operator['Operator']+","+str(current_timestamp)+","+str(start_date)+","+ str(finish_date)+","+ str(TotalEnergyDelivered['TotalEnergyDelivered'])+","+str(NumberofActivePoints)+","+str(ActivePointsList[i]["PointID"])+","+str(ActivePointsList[i]["PointSessions"])+","+str(ActivePointsList[i]["EnergyDelivered"])+"\n"
			i=i+1
		return Response(csv, mimetype='text/csv')
	else:
		return Response(status=400)



#🟩🟩🟩🟧🟧🟧🟧🟧🟧🟩🟩🟩-- 2c SessionsPerEV --🟩🟩🟩🟧🟧🟧🟧🟧🟧🟩🟩🟩

@baseURL.route('/SessionsPerEV/<vehicleID>/<yyyymmdd_from>/<yyyymmdd_to>', methods=['GET'])
@jwt_required()
def SessionsPerEV(vehicleID, yyyymmdd_from, yyyymmdd_to):
	#parse the args
	g.stationID = vehicleID
	g.yyyymmdd_from = yyyymmdd_from
	g.yyyymmdd_to = yyyymmdd_to

	#check point ID
	if (not(vehicleID.isdigit()) or not(yyyymmdd_from.isdigit()) or not(yyyymmdd_to.isdigit())):
		return Response(status=400)

	vehicle_exists = db_read("""SELECT * FROM Vehicle WHERE VehicleID = %s""", (int(vehicleID),))

	if (len(vehicle_exists) == 0): #no such a point
		return Response(status=400)


	#check year

	start_year = yyyymmdd_from[0] + yyyymmdd_from[1] + yyyymmdd_from[2] + yyyymmdd_from[3]
	finish_year = yyyymmdd_to[0] + yyyymmdd_to[1] + yyyymmdd_to[2] + yyyymmdd_to[3]

	current_year = datetime.datetime.now().year

	if ((int(finish_year)>int(current_year)) or (int(finish_year)<int(start_year))):
		return Response(status=400)

	#check month
	start_month = yyyymmdd_from[4] + yyyymmdd_from[5]
	finish_month = yyyymmdd_to[4] + yyyymmdd_to[5]

	if ((int(start_month)>13) or (int(finish_month)>13) or (int(start_month)<1) or (int(finish_month)<0) ):
		return Response(status=400)

	#check day
	start_day = yyyymmdd_from[6] + yyyymmdd_from[7]
	finish_day = yyyymmdd_to[6] + yyyymmdd_to[7]

	if ((int(start_day)>31) or (int(finish_day)>31) or (int(start_day)<1) or (int(finish_day)<0)):
		return Response(status=400)

	start_date=start_year+"-"+start_month+"-"+start_day
	finish_date=finish_year+"-"+finish_month+"-"+finish_day

	current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


	TotalEnergyDeliveredlist = db_read("""SELECT FORMAT(SUM(EnergyDelivered),2) AS TotalEnergyDelivered FROM  session WHERE VehicleID=%s AND DATE(FinishedON) BETWEEN %s AND %s""",(vehicleID, start_date, finish_date))
	TotalEnergyDelivered=TotalEnergyDeliveredlist[0]
	VisitedPointslist = db_read("""SELECT COUNT(PointID) AS NumberOfVisitedPoints FROM  session WHERE VehicleID=%s AND DATE(FinishedON) BETWEEN %s AND %s""",(vehicleID, start_date, finish_date))
	VisitedPoints=VisitedPointslist[0]
	db_write("""SET @rank=0;""",())
	VehicleChargingSessionsList = db_read(""" SELECT @rank:=@rank+1 AS SessionIndex, SessionID, Pr.Name, StartedOn, FinishedOn, FORMAT(EnergyDelivered,2) AS EnergyDelivered, PricePolicyRef, FORMAT(CostPerKWh,2), FORMAT(SessionCost,2)  FROM session INNER JOIN Provider AS Pr USING (ProviderID) WHERE vehicleID=%s AND DATE(FinishedON) BETWEEN %s AND %s""",(int(vehicleID), start_date, finish_date))
	NumberOfVehicleChargingSessions = len(VehicleChargingSessionsList)

	#special date format

	for i in range(len(VehicleChargingSessionsList)):
		VehicleChargingSessionsList[i]["StartedOn"]=VehicleChargingSessionsList[i]["StartedOn"].strftime("%Y-%m-%d %H:%M:%S")
		VehicleChargingSessionsList[i]["FinishedOn"]=VehicleChargingSessionsList[i]["FinishedOn"].strftime("%Y-%m-%d %H:%M:%S")


	return jsonify(VehicleID=vehicleID, RequestTimestamp=current_timestamp, PeriodFrom=start_date, PeriodTo=finish_date, TotalEnergyDelivered=TotalEnergyDelivered['TotalEnergyDelivered'], NumberOfVisitedPoints=VisitedPoints['NumberOfVisitedPoints'], NumberOfVehicleChargingSessions=NumberOfVehicleChargingSessions, VehicleChargingSessionsList=VehicleChargingSessionsList)


#🟩🟩🟩🟩🟧🟧🟧🟧🟩🟩🟩🟩-- 2d SessionsPerProvider --🟩🟩🟩🟩🟧🟧🟧🟧🟩🟩🟩🟩

@baseURL.route('/SessionsPerProvider/<providerID>/<yyyymmdd_from>/<yyyymmdd_to>', methods=['GET'])
@jwt_required()
def SessionsPerProvider(providerID, yyyymmdd_from, yyyymmdd_to):
	#parse the args
	g.providerID = providerID
	g.yyyymmdd_from = yyyymmdd_from
	g.yyyymmdd_to = yyyymmdd_to

	#check point ID
	if (not(providerID.isdigit()) or not(yyyymmdd_from.isdigit()) or not(yyyymmdd_to.isdigit())):
		return Response(status=400)

	provider_exists = db_read("""SELECT * FROM Provider WHERE ProviderID = %s""", (int(providerID),))

	if (len(provider_exists) == 0): #no such a point
		return Response(status=400)


	#check year

	start_year = yyyymmdd_from[0] + yyyymmdd_from[1] + yyyymmdd_from[2] + yyyymmdd_from[3]
	finish_year = yyyymmdd_to[0] + yyyymmdd_to[1] + yyyymmdd_to[2] + yyyymmdd_to[3]

	current_year = datetime.datetime.now().year

	if ((int(finish_year)>int(current_year)) or (int(finish_year)<int(start_year))):
		return Response(status=400)

	#check month
	start_month = yyyymmdd_from[4] + yyyymmdd_from[5]
	finish_month = yyyymmdd_to[4] + yyyymmdd_to[5]

	if ((int(start_month)>13) or (int(finish_month)>13) or (int(start_month)<1) or (int(finish_month)<0) ):
		return Response(status=400)

	#check day
	start_day = yyyymmdd_from[6] + yyyymmdd_from[7]
	finish_day = yyyymmdd_to[6] + yyyymmdd_to[7]

	if ((int(start_day)>31) or (int(finish_day)>31) or (int(start_day)<1) or (int(finish_day)<0)):
		return Response(status=400)

	start_date=start_year+"-"+start_month+"-"+start_day
	finish_date=finish_year+"-"+finish_month+"-"+finish_day

	ProviderSession=db_read("""SELECT
	Pr.ProviderID,
	Pr.Name AS ProviderName,
	Ch.StationID AS StationID,
	se.SessionID,
	se.VehicleID,
	se.StartedOn,
	se.FinishedOn,
	FORMAT(se.EnergyDelivered, 2) AS EnergyDelivered,
	se.PricePolicyRef,
	FORMAT(se.CostPerKWh,2) AS CostPerKWh,
	FORMAT(se.SessionCost,2) AS TotalCost
	FROM
	session se
	INNER JOIN Chargingpoint ch USING(PointID) INNER JOIN Provider pr USING (ProviderID)
	WHERE se.providerID=%s AND DATE(se.FinishedON) BETWEEN %s AND %s""",(int(providerID), start_date, finish_date))

	for i in range(len(ProviderSession)):
		ProviderSession[i]["StartedOn"]=ProviderSession[i]["StartedOn"].strftime("%Y-%m-%d %H:%M:%S")
		ProviderSession[i]["FinishedOn"]=ProviderSession[i]["FinishedOn"].strftime("%Y-%m-%d %H:%M:%S")


	return jsonify(sessions=ProviderSession)






#@@@@@@@@@@@@@@@@@@@ CUSTOM ROUTE@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#to avoid some problems with dependecies put this line of code at EOF

app.register_blueprint(baseURL, url_prefix="/evcharge/api")
