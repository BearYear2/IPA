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

from flask.json import jsonify
import Modules.MyApp as flApp

import Modules.MyDatabase as MyDatabase
import Modules.MyUser as MyUser
import Modules.MyCalendar as MyCalendar


from werkzeug.security import generate_password_hash, check_password_hash


app = flApp.flaskApp
request = flApp.request


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/home')
def home():
    #do some meta-magic
    return "Up and running"

@app.route('/calendar')
def calendar():
    data = request.get_json()
    if MyDatabase.dFetch_data(data["token"]):
        if data["action"] == "ret":
            return MyCalendar.cRetrieveDate(data["token"],data["date"])
        if data["action"] == "reg":
            return MyCalendar.cRegisterDate(data["token"],data["date"])
        if data["action"] == "chk":
            return MyCalendar.cIsAvailable(data["token"],data["date"])

@app.route('/login', methods =['POST'])
def login():
    user_data = request.get_json()
    answer = None
    password = {"password":generate_password_hash(user_data["password"])}
    if MyUser.uLogin(user_data["user"],password):
        inp = [user_data["user"],password]
        res = ["token"]
        MyDatabase.dFetch_data(inp)
        token = res
        if token:
            answer = jsonify({'token':token})
            res = ["role"]
            MyDatabase.dFetch_data(answer,res)
            #auth.current_user = res
            return answer
        else:
            answer = jsonify({'token':False})
            return answer
    else:
        answer = jsonify({'token':False})
        return answer
#@auth.error_handler
def auth_error():
    return jsonify({'message':'Invalid credentials'})

@app.route('/register', methods =['POST'])
def register():
    user_data = request.get_json()
    if MyUser.uRegister(user_data):
        password = {"password":generate_password_hash(user_data["password"])}
        req = [user_data["user"],password, user_data["role"]]
        token = MyDatabase.dFetch_data(req)
        if token:
            return token
        else:
            return MyUser.uGenerate_token(user_data["user"], user_data["password"]) 
    else:
        return MyUser.uGenerate_error(user_data)

@app.route('/appointments')
def appointments():
    data = request.get_json()
    if MyUser.uLogin(data["token"]):
        return MyCalendar.cRetrieveDate(data["token"], data["date"])

@app.route('/book')
def book():
    data = request.get_json()
    if MyUser.uLogin(data["token"]):
        
        return MyUser.uBook(data["user"], data["date"])


@app.route('/admin')
def admin():
    data = request.get_json()
    if MyUser.uLogin(data["token"]) == "a":
        password = {"password",generate_password_hash(data["password"])}
        return MyUser.uAllowRegistration(data["user"], password)



@app.errorhandler(404)
def pageNotFound(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        answer = jsonify({'error':'not found'})
        answer.status_code = 404
        return answer
    return app.render_template('404.html'), 404
@app.errorhandler(500)
def internalBreakdown(e):
    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        answer = jsonify({'error':'internal servr error','message':e})
        answer.status_code = 500
        return answer
    return app.render_template('500.html'), 500

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