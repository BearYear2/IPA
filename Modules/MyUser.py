#return user, nurse or admin
#token and type (token is user identifier)
#receive username and pass from a post request
#at register generate token
#how do you receive post?

#Don't forget about JSON
import re
from flask import json

from flask.json import jsonify
#from MyDatabase import dFetch_data, dSend_data
from . import MyDatabase
#from MyApp import *
from . import MyApp
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, exc



def uGenerate_token(username, password):
    #token expires in a day
    token = Serializer(MyApp.flaskApp.config['SECRET_KEY'],expires_in=86400)
    token = token.dumps({'id':username}).decode('utf-8')
    return token

def uGenerate_error(json_data):
    return "bad"

def uVerify_token(token):
    exist = MyDatabase.dFetch_data({"token":token})
    if exist:
        return True
    else:
        return False

def uGetRole(token):
    return MyDatabase.dFetch_data({"token":token})

def uRegister(user, password):
    token = uGenerate_token(user,password)
    answer = False
    req = {"user":user,"password":password,"token":token}
    MyDatabase.dSend_data(req,answer)
    return answer

def uLogin(user, password):
    if MyDatabase.dFetch_data({"user":user,"password":password}):
        return MyDatabase.dFetch_data(uGenerate_token(user,password))
def uCheckUser(json_data):
    user = json_data["user"]
    password = json_data["password"]
    token = json_data["token"]
    #if no user is provided then check for token
    if user == '':
        #if token is not provided, no loging is possible, return error?
        if token == '':
            return uGenerate_error("No credentials provided")
        else:
            #does this token exist in our db
            return uVerify_token(token)
        
        

#User
def uBook():
    pass
def uAppointments():
    pass

#Medic
def uAllowBook():
    pass
def uCheckAppoints():
    pass
def uCheckPatients():
    pass

#Nurse
def uAllowBookFor():
    pass

#Admin
def uAllowRegistration():
    pass