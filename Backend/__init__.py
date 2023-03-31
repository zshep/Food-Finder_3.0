from flask import Flask
from Backend.routes import home 
from flask_pymongo import PyMongo




def create_app(test_config=None):
  #set up app config
  app = Flask('Backend', static_url_path='/')
  app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/mydb"
  mongo = PyMongo(app)

  #creating the food collection
  food_collection = mongo.db.foods



  #route for server
  @app.route('/')
  def server():
    return 'the force is strong with you, but your not a jedi yet'
  
  #register routes
  app.register_blueprint(home)

  init_db(app)

  return app