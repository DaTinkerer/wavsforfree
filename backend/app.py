from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
from decouple import config
import requests

app = Flask(__name__)
app.secret_key = config("SECRET_KEY")
CORS(app)
api_key = config("key")