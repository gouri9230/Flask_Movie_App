from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)

db = SQLAlchemy()

# Creating the app configurations
app.config["SECRET_KEY"] = "fjklajgrighrueia"
app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:////home/shrigouri/database.db'

login_manager = LoginManager()

# prefix the endpoint with the blueprint name where it is located
login_manager.login_view = "auth.login" 

# Initializing flask extensions
db.init_app(app)
login_manager.init_app(app)

from app.authentication import auth
from app.movie import mov

#Register blueprints
app.register_blueprint(auth)
app.register_blueprint(mov, url_prefix="/mov")

#optional: to printout the url path of each endpoint
print(app.url_map)

with app.app_context():
    db.create_all()

