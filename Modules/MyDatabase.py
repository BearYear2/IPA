#return Response(response = json.dumps(<key1>:<value1>,....),status = <status_code>, mimetype = "application/json")
#save as many types of fields as you want
#app.route("/user/<idxx>")
#def f(idxx):
from ctypes import resize
#from MyApp import *
from . import MyApp
from flask import Response



def dFetch_data(input):
    #input = {<key1>:<value to look for>, <key2>:<value to look for>,....}
    result = list(MyApp.mongo.db.clinic.users.find_one(input))
    return result

def dSend_data(content):
    result = False
    for k in content.keys():
        result = MyApp.mongo.db.clinic.users.insert_one({k:content[k]})
        if result["writeConcernError"]:
            return False
    return True

def dModify_data(input):
    result = MyApp.mongo.db.clinic.users.update_one({"name":"something"},{"$set":input})
    return result.raw_result["updatedExisting"] and result.raw_result["nModified"] == 1 

def dDelete_data(input):
    #it exists if fetch successfully
    result = MyApp.mongo.db.clinic.users.delete_one({"name":"something"})
    return result.raw_result["n"] == 1