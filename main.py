from flask import Flask
app = Flask(__name__)
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
auth = HTTPBasicAuth()

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/home')
@auth.login_required
def home():
    return '<h1>Hello Stranger!</h1>'

@app.route('/calendar')
@auth.login_required
def calendar():
    return '<h1>Today is not the day</h1>'

@app.route('/login')
def login():
    return '<h1>Are you here to define yourself?</h1>'

@app.route('/register')
def register():
    return '<h1>Are you here to introduce yourself?</h1>'

@app.route('/appointments')
@auth.login_required
def appointments():
    return '<h1>You are indeed not busy today</h1>'

@app.route('/book')
@auth.login_required
def book():
    return '<h1>You cannot use this feature yet</h1>'

@app.route('/admin')
@auth.login_required
def admin():
    return '<h1>You have the power!!</h1>'

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