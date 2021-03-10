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
# pip install -r requirements.txt

#export FLASK_APP=api.py
#export FLASK_ENV=development       !!FOR DEBUG MODE!!
#flask run -h localhost -p 8765 --cert=adhoc


#@@@@@@@@@@@@@@@@@@@@@@-- Modules --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Some libraries might be useless (copied-pasted from online tutorials)
from flask import Flask, Blueprint
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import flask_restx
from flask_mysqldb import MySQL
import mysql.connector

#@@@@@@@@@@@@@@@@@@@@@@-- Api Creation --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

app = Flask(__name__)

if __name__ == "__main__":
	app.run(debug=True)


#@@@@@@@@@@@@@@@@@@@@@@-- DB conection --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   TODO: Should be in a seperate file
#   we are using the default port 3306

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sqlpassword'
app.config['MYSQL_DB'] = 'project_e_lectra'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' #optional


mysql = MySQL(app)

#@@@@@@@@@@@@@@@@@@@@@@-- DB Healhcheck --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#   This is an auxilary endpoint that shows the user that the DB is connected
#   and works properly.

@app.route('/demo', methods=['GET'])
def home():
    return '''<h1>Nothing to see here</h1>
<p>Except this marvelous paragraph, shows that everything is OK</p>'''


@app.route('/admin/healthcheck', methods=['GET'])
def healthcheck():
	cur = mysql.connection.cursor()
	cur.execute("SELECT * FROM user")
	mysql.connection.commit()
	cur.close()
	return {"status":"OK"}
