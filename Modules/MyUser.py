#return user, nurse or admin
#token and type (token is user identifier)
#receive username and pass from a post request
#at register generate token
#how do you receive post?

#Don't forget about JSON
import re
from flask import json

from flask.json import jsonify
from flask.wrappers import Response
#from MyDatabase import dFetch_data, dSend_data
from . import MyDatabase
#from MyApp import *
from . import MyApp
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, exc



def uGenerate_token(username, password):
    #token expires in a day
    token = Serializer("Once upon a middle land, close, nearby, lived a king, a queen, and a small prince.",expires_in=86400)
    token = token.dumps({'id':username, 'id_':password}).decode('utf-8')
    MyDatabase.dModify_data({"user":username,"password":password},{"token":token})
    return token


def uVerify_token(token):
    s = Serializer("Once upon a middle land, close, nearby, lived a king, a queen, and a small prince.")
    try:
        data = s.loads(token)
    except:
        return False
    return True
    

def uGetRole(token):
    return MyDatabase.dFetch_data({"token":token})

def uRegister(user, password):
    print("\n\n\nIN REGISTER\n\n\n")
    token = uGenerate_token(user,password)
    response = MyDatabase.dSend_data({"user":user,"password":password,"token":token})
    print(response)
    if response:
        print(token)
        return token
    return False

def uLogin(user, password):
    print("\n\n\nIN LOGIN\n\n\n")
    fetchRes = MyDatabase.dFetch_data({"user":user})#,"password":password})
    print(fetchRes)
    if fetchRes != None:
        if fetchRes["token"]:
            print(fetchRes["token"])
            if uVerify_token(fetchRes["token"]):
                return fetchRes["token"]
            else:
                return uGenerate_token(user,password)
        else:
            return False
    else:
        return False
def uCheckUser(json_data):
    user = json_data["user"]
    password = json_data["password"]
    token = json_data["token"]
    #if no user is provided then check for token
    if user == '':
        #if token is not provided, no loging is possible, return error?
        if token == '':
            #return uGenerate_error("No credentials provided")
            pass
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