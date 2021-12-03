#return user, nurse or admin
#token and type (token is user identifier)
#receive username and pass from a post request
#at register generate token
#how do you receive post?

#Don't forget about JSON
import json
from WT_Project.database import *
import database

def uGenerate_token(username, password):
    #meta-magic token creation
    token = []
    return token
def uGenerate_error(json_data):
    return "bad"
#User
def uRegister(user, password):
    token = uGenerate_token(user,password)
    dSend_data(token)
    return True
def uLogin(user, password):
    if dFetch_data(user) and dFetch_data(password):
        return dFetch_data(uGenerate_token(user,password))

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