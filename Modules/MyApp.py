from flask import Flask, request

from flask.templating import render_template
from flask_pymongo import PyMongo
import pymongo


flaskApp = Flask(__name__)
try:
    mongo = pymongo.MongoClient(
        host = "localhost",
        port = 27017,
        serverSelectionTimeoutMS = 100
    )
    mongo.server_info()
except:
    print("error when connecting to mongodb")

