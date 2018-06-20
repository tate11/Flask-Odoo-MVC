from flask import Flask
from ..config.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


#Flask project initialization configs
app=Flask(__name__,template_folder='../templates',static_folder="../static")
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.init_app(app)
login.login_view = 'login'
