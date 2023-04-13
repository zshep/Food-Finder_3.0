from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.flask_db
foods = db.foods


@app.route('/')
def index():

    return "hello Shep"

@app.route('/jedi')
def jedi():
    
    return "the force is strong with you, but you're not a jedi yet"