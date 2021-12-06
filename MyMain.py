#Status codes
#200 OK
#201 Created
#202 Accepted
#204 No content
#401 Unauthorized
#403 Forbidden
#404 Not Found
#405 Method Not Allowed
#500 Internal Server Error

from ctypes import resize
import re

import json

from flask.json import jsonify
from flask.templating import render_template
from flask.wrappers import Response
import Modules.MyApp as flApp

import Modules.MyDatabase as MyDatabase
import Modules.MyUser as MyUser
import Modules.MyCalendar as MyCalendar


from werkzeug.security import generate_password_hash, check_password_hash


app = flApp.flaskApp
request = flApp.request


@app.route('/')
def index():
    return Response(
            response= json.dumps({'message':'Good Work'}),
            status = 200,
            mimetype="application/json"
        )

@app.route('/home')
def home():
    return Response(
            response= json.dumps({'message':'Good Work'}),
            status = 200,
            mimetype="application/json"
        )

@app.route('/calendar', methods = ['Get', 'POST'])
def calendar():
    data = request.get_json()
    if MyDatabase.dFetch_data(data["token"]):
        if request.method == 'POST':
            return Response(
                response = json.dumps(MyCalendar.cRegisterDate(data["token"],data["date"])),
                status = 200,
                mimetype = "application/json"
            )
        if request.method == 'GET':
            return Response(
                response = json.dumps(MyCalendar.cRetrieveDate(data["token"],data["date"])),
                status = 200,
                mimetype = "application/json"
            )
    else:
        return Response(
        response= json.dumps({'message':'Invalid token provided', 'error':'Bad Request'}),
        status = 400,
        mimetype="application/json"
        )
    
    
@app.route('/login', methods =['POST', 'GET'])
def login():
    user_data = request.get_json()
    user = user_data["user"]
    password = {"password":generate_password_hash(user_data["password"])}
    token = MyUser.uLogin(user,password)
    if token:
        return Response(
            response = json.dumps({"token":token}),
            status = 200,
            mimetype = "application/json"
            )
    else:
        return Response(
            response = json.dumps({'message':'Invalid token or token expired'}),
            status = 400,
            mimetype = "application/json"
        )



@app.route('/register', methods =['POST', 'GET'])
def register():
    user_data = request.get_json(force=True)
    user = user_data["user"]
    password = generate_password_hash(user_data["password"])
    if MyUser.uLogin(user,password):
        return Response(
            response = json.dumps({"message":"User already exists in the database", 'error':"User exists"}),
            status = 400,
            mimetype = "application/json"
        )
    else:
        token = MyUser.uRegister(user, password)
        if token:
            return Response(
            response = json.dumps({"message":"user created", "token":token}),
            status = 200,
            mimetype = "application/json"
        )
        else:
            return Response(
            response = json.dumps({"message":"Token could not be created", 'error':"Bad token"}),
            status = 500,
            mimetype = "application/json"
        )

@app.route('/appointments', methods =['GET'])
def appointments():
    data = request.get_json()
    if MyUser.uLogin(data["token"]):
        return MyCalendar.cRetrieveDate(data["token"], data["date"])

@app.route('/book', methods =['POST'])
def book():
    data = request.get_json()
    if MyUser.uLogin(data["token"]):
        
        return MyUser.uBook(data["user"], data["date"])


@app.route('/admin', methods = ['POST'])
def admin():
    data = request.get_json(force=True)
    success = MyDatabase.dSend_data(data)
    print(data)
    if data == None:
        return Response(
            response= json.dumps({'error':'resource not found','message':"error"}),
            status = 500,
            mimetype="application/json"
        )
    #if success == True:
       # return Response(
        #        response= json.dumps({'content':data,'message':"added "}),
         #       status = 200,
         #       mimetype="application/json"
        #    )
    return Response(
                response= json.dumps({'content':data,'message':"not much"}),
                status = 200,
                mimetype="application/json"
            )

@app.errorhandler(404)
def pageNotFound(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        return Response(
        response= json.dumps({'error':'resource not found','message':"error"}),
        status = 404,
        mimetype="application/json"
    )
    return Response(response= ("<h1>Error 404</h1>"),status = 404, mimetype="application/html")
@app.errorhandler(500)
def internalBreakdown(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        #answer = jsonify({'error':'internal servr error','message':e})
        #answer.status_code = 500
        #return answer
        return Response(
        response= json.dumps({'error':'internal servr error','message':"error"}),
        status = 500,
        mimetype="application/json"
    )
    return Response(response= ("<h1>Error 500</h1>"),status = 500, mimetype="application/html")

app.run(debug=True)


#Things to be dealt with
    #Display main page
    #Allow user authentification (either login or register)
        #Allow pass reset?
    #Define user types (Admin, Medic, Nurse and Patient)
    #Admin has only confirmation dashboard (he sees names, and some other login details, and decides permissions)
    #Medics have a calendar, a list of nurses(?), and booked patients
    #Nurses have a calendar, and booked patients
    #Patients have a calendar 