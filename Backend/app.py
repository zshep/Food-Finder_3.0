from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
foods = db.foods
