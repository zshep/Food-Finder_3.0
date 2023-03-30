from flask import Flask
from Backend.routes import home 
from pymongo import MongoClient


# setting up mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client.food_database

def create_app(test_config=None):
  #set up app config
  app = Flask('Backend', static_url_path='/')



  #route for server
  @app.route('/')
  def server():
    return 'the force is strong with you, but your not a jedi yet'
  
  #register routes
  app.register_blueprint(home)

  init_db(app)

  return app