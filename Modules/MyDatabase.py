#return Response(response = json.dumps(<key1>:<value1>,....),status = <status_code>, mimetype = "application/json")
#save as many types of fields as you want
#app.route("/user/<idxx>")
#def f(idxx):
from ctypes import resize
#from MyApp import *
from . import MyApp
from flask import Response
from bson import json_util
import json


def dFetch_data(content):
    query = json.loads(json_util.dumps(content))
    print("query:")
    print(query)
    #input = {<key1>:<value to look for>, <key2>:<value to look for>,....}
    result = MyApp.mongo.db.clinic.users.find_one(query)
    return result

def dSend_data(content):
    query = json.loads(json_util.dumps(content))
    result =MyApp.mongo.db.clinic.users.insert_one(query)
    #if result["writeConcernError"]:
    #    return False
    return result.inserted_id

def dModify_data(searchby,content):
    query = json.loads(json_util.dumps(content))
    filter = json.loads(json_util.dumps(searchby))
    result = MyApp.mongo.db.clinic.users.update_one(filter,{"$set":query})
    return result.raw_result["updatedExisting"] and result.raw_result["nModified"] == 1 

def dDelete_data(content):
    #it exists if fetch successfully
    if dFetch_data(content):
        query = json.loads(json_util.dumps(content))
        result = MyApp.mongo.db.clinic.users.delete_one(query)
        return result.raw_result["n"] == 1
    else:
        #No user to delete, so we did not delete anything
        return False