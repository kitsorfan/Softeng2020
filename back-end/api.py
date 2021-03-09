# e-Lectra Project by The Charging Aces:
# ~Stelios Kandylakis
# ~ Margarita  Oikonomakou
# ~Kitsos     Orfanopoulos
# ~Vasilis    Papalexis
# ~Georgia    Stamou
# ~Dido       Stoikou
# Softeng, ECE NTUA, 2021

# API code

# --------------Prerequisites-----------------
# pip3 install requests
# pip install Flask-JWT

#----------------

# How to run the Flask server
#1. open the terminal.
#2. type
#               export FLASK_APP=api.py
#3.then type
#               flask run -h localhost -p 8765 --cert=adhoc
#4. Go to your browser at:
#               https://localhost:8765/



#@@@@@@@@@@@@@@@@@@@@@@-- Libraries --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Some libraries might be useless (copied-pasted from online tutorials)

from flask import Flask, Blueprint, abort, request
from werkzeug.security import safe_str_cmp
from flask import Flask
from flask_restx import Api, Resource, fields
from werkzeug.utils import cached_property
from flask_jwt import JWT, jwt_required, current_identity
from flask_cors import CORS
from flask_cors import CORS
import requests
from date import datetime
from datetime import date
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
import sqlQueries
import os
import errors
import hashlib
import mysql.connector

#@@@@@@@@@@@@@@@@@@@@@@-- API creation --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

app = Flask(__name__)
api = Api(app)

#@@@@@@@@@@@@@@@@@@@@@@-- JWT configuration --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
app.config['JWT_SECRET_KEY'] = 'demonstration'
app.config['SWAGGER_UI_JSONEDITOR'] = True

CORS(app, resources={r'/*': {'origins': '*'}})

jwt = JWTManager(app)


#@@@@@@@@@@@@@@@@@@@@@@-- Authorizaztions --@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#====================User============================
@api.route('/user/<UserID>/check_auth')
class UserAuth(Resource):
    @jwt_required()
    def get(self, user_id):
        try:
            if (get_jwt_identity() != user_id):
                raise errors.NotAuthorized
            else:
                return {
                    'msg' : 'Authorized'
                }
        except errors.NotAuthorized as error:
            abort(401, str(error))

#====================Admin============================
@api.route('/admin/<AdminID>/check_auth')
class UserAuth(Resource):
    @jwt_required()
    def get(self, admin_id):
        try:
            if (get_jwt_identity() != admin_id):
                raise errors.NotAuthorized
            else:
                return {
                    'msg' : 'Authorized'
                }
        except errors.NotAuthorized as error:
            abort(401, str(error))
#________________________________________________________________________________________________
