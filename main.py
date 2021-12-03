import re
from flask import Flask
from flask import request
from flask_httpauth import HTTPBasicAuth

from WT_Project.user import *
from WT_Project.calendar import *
from WT_Project.database import *
#from json import *

from werkzeug.security import generate_password_hash, check_password_hash


auth = HTTPBasicAuth()
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/home')
@auth.login_required
def home():
    #do some meta-magic
    return "Up and running"

@app.route('/calendar')
@auth.login_required
def calendar():
    data = request.get_json()
    if dFetch_data(data["token"]):
        if data["action"] == "ret":
            return cRetrieveDate(data["token"],data["date"])
        if data["action"] == "reg":
            return cRegisterDate(data["token"],data["date"])
        if data["action"] == "chk":
            return cIsAvailable(data["token"],data["date"])

@app.route('/login')
def login():
    user_data = request.get_json()
    if uLogin(user_data):
        req = [user_data["user"],user_data["password"]]
        token = dFetch_data(req)
        if token:
            return token
        else:
            return "Bad thing"
    else:
        return "User not recognized"

@app.route('/register')
def register():
    user_data = request.get_json()
    if uRegister(user_data):
        req = [user_data["user"],user_data["password"]]
        token = dFetch_data(req)
        if token:
            return token
        else:
            return uGenerate_token(user_data["user"], user_data["password"]) 
    else:
        return uGenerate_error(user_data)

@app.route('/appointments')
@auth.login_required
def appointments():
    data = request.get_json()
    if uLogin(data["token"]):
        return cRetrieveDate(data["token"], data["date"])

@app.route('/book')
@auth.login_required
def book():
    data = request.get_json()
    if uLogin(data["token"]):
        return cRegisterDate(data["token"], data["date"])

@app.route('/admin')
@auth.login_required
def admin():
    data = request.get_json()
    if uLogin(data["token"]) == "a":
        return uAllowRegistration(data["user"], data["password"])

app.run()

#Things to be dealt with
    #Display main page
    #Allow user authentification (either login or register)
        #Allow pass reset?
    #Define user types (Admin, Medic, Nurse and Patient)
    #Admin has only confirmation dashboard (he sees names, and some other login details, and decides permissions)
    #Medics have a calendar, a list of nurses(?), and booked patients
    #Nurses have a calendar, and booked patients
    #Patients have a calendar 