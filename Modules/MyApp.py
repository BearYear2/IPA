from flask import Flask, request

from flask.templating import render_template
from flask_pymongo import PyMongo


flaskApp = Flask(__name__)
flaskApp.config["MONGO_URI"] = "mongodb://dummyDb"
mongo = PyMongo(flaskApp)

