shell_data = """

echo "###############################################################################"
echo "                              Running Flask App  v1.0                              "
echo "###############################################################################"

file="db.conf"

# Functions to be used in configurations

function flask_config_db() {
  echo ""
  echo " Getting database configs....."
  echo "-----------------------------------------------------------------------------"
  echo "(+) Enter RDBMS type:"
  read db_type
  echo "-----------------------------------------------------------------------------"
  echo "(+) Enter host name/ip:"
  read db_host
  echo "-----------------------------------------------------------------------------"
  echo "(+) Enter Database name:"
  read db_name
  echo "-----------------------------------------------------------------------------"
  echo "(+) Enter Database user:"
  read db_user
  echo "-----------------------------------------------------------------------------"
  echo "(+) Enter Database password:"
  read db_passwd
  echo "-----------------------------------------------------------------------------"
  echo "(+) Enter Database port:"
  read db_port
  echo "-----------------------------------------------------------------------------"
  echo "$db_type://$db_user:$db_passwd@$db_host:$db_port/$db_name" > db.conf
  echo "DB configs saved to db.conf file successfully!!!"
  echo ""
  export FLASK_APP=$flask_app
  export DATABASE_URL='$db_type://$db_user:$db_passwd@$db_host:$db_port/$db_name'
  export FLASK_DEBUG=$debug
  export FLASK_ENV=$mode

  echo "Running flask project....."
  flask run
}


function flask_run() {
	if [ -s "$file" ]
  then
    db_access=$(head -n 1 $file)
    export FLASK_APP=$flask_app
    export DATABASE_URL=$db_access
    export FLASK_DEBUG=$debug
    export FLASK_ENV=$mode
    echo "Running flask project....."
    flask run

  else
    flask_config_db

fi
}



echo "                          Get Flask Application Configs"
echo "-------------------------------------------------------------------------------"
echo "(+) Enter main flask app file:"
read flask_app
echo "-------------------------------------------------------------------------------"
echo "(+) Enter mode to use (development or production):"
read mode
echo "-------------------------------------------------------------------------------"
echo "(+) Enter debug (True or False):"
read debug
echo "-------------------------------------------------------------------------------"
echo ""
echo "###############################################################################"

if [ -f "$file" ]
then
    flask_run
else
    flask_config_db
fi

"""



readme_data="""


                        #  **Flask Project Folder Structure v1.0**
              ---------------------------------------------------------

This repo is a demonstration of how one can structure Flask projects. It is
a fork of Odoo's module structure, thus might relate well with Odoo users
interested in flask. Its not a standard flask project structure, but a reflection
of how it can be done among many other concepts out there. This is version 1.0 hopefully
others will improve on it, patch it etc.


Below is the structure, better viewed in an editor e.g _atom_:


                              #   **Module Structure**
                    -------------------------------------------------
* **uploads** _(optional)_

* **Project_folder**
     * _config_
     * _controllers_
     * _data_
     * _doc_
     * _forms_
     * _il8n_
     * _models_
     * _migrations_
     * _static_
     * _templates_

* **main_app.py**
* **init__.py**
* **run_app.sh**






                                **Definitions**
                            ------------------------

  (+) **app_config**
  ----------------------------------------------------------
  This contains all configurations regarding the application being
  created. configs based on modules flask-login, flask-wtf etc.


  (+) **config**
  --------------------
  Stores flask and project configurations


  (+) **controllers**
  ---------------------
  Contains a file routes.py stores URL controller functions to
  link to views.


  (+) **data**
  ----------------------
  Stores csv,excel data mainly used as imports or export.


  (+) **doc**
  ------------------------------
  Contains documentation in relation to the module files.


  (+) **forms**
  -----------------------
  Used as model for web forms such as contact us, login, registration forms.


  (+)**i18n**
  ------------------------
  Used for language translation .po files



  (+)**models**
  ----------------------------------------------------------------
  Used to create models to be used as db fields by forms
  ----------------------------------------------------------------

  (+) **migrations**
  -----------------------------------------------------------------
  This folder is created when using the flask-migrate commands.
  It requires alembic to work, but bottom line is, it generates
  a migration folder when executing _flask db init_


  (+)**static**
  ----------------------------------------------------------------
  Stores CSS, JS, Font, Img files and scripts.


  (+)**templates**
  ----------------------------------------------------------------
  Flask looks for this folder to find views to display content
  to uses. Used in conjunction with controllers.


  (+)**main_app.py**
  ----------------------------------------------------------------
  Flask uses this with its FLASK_APP environment variable to load
  the flask app.


  (+)**run_app.sh**
  ----------------------------------------------------------------
  A simple shell script to run your application. It generates and configures _db.conf_ file, _main_app.py_ , _debug_ and project _dev mode_ environment varibles for linux. May not be necessarily used but can be tweaked
  to run your project.

  (+)**uploads**
  ---------------------------------------------------------------------
  You can store uploaded files, images etc. This is optional, but remember that its
  best to store files on disk, then store the path in the database for efficient db_access
  and not clog the db space.
  --------------------------------------------------------------------------





                        #      **Major Requirements**
                      ----------------------------------------
  The major package requirements currently for this project are:

  * Flask==1.0.2
  * Flask-Login==0.4.1
  * Flask-Migrate==2.1.1
  * Flask-SQLAlchemy==2.3.2
  * Flask-WTF==0.14.2
  * psycopg2==2.7.4
  * psycopg2-binary==2.7.4

_pip install <package>_ or _pip install -r doc/requirements.txt_





                            #     **How To Use It**
                      -----------------------------------

  To test the Structure, follow the below instructions:

  * (+) virtualenv -p python3 flask-projects-exec
  * (+) git clone https://kkamaa@bitbucket.org/kkamaa/flask-project.git
  * (+) source flask-project/bin/activate
  * (+) cd flask-project
  * (+) cd flask-app
  * (+) cd doc
  * (+) pip install -r requirements.txt
  * (+) cd ..
  * (+) chmod +x run_app.sh
  * (+) ./run_app.sh
      * main_app.py
      * development
      * True

"""

main_application_data = """
# from .app_config.app_config import app,db
# from .models.models import User, Post
#
# @app.shell_context_processor
# def make_shell_context():
#     return {'db': db, 'User': User, 'Post': Post}


"""
init_main="""from . import controllers,models,app_config,forms"""

models_data="""
# from ..app_config.app_config import db,login
# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash
# from datetime import datetime
#
# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     gender=db.Column(db.String(6))
#     password_hash = db.Column(db.String(128))
#
#
#     @login.user_loader
#     def load_user(id):
#         return User.query.get(int(id))
#
#     def __repr__(self):
#         return '<User {}>'.format(self.username)
#
#     def set_password(self, password):
#         self.password_hash = generate_password_hash(password)
#
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
#
#
# class Contact_us(db.Model):
#     id=db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(120))
#     email=db.Column(db.String(120))
#     comment=db.Column(db.String(250))
#
#
# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#
#     def __repr__(self):
#         return '<Post {}>'.format(self.body)


"""
init_models_data="""from . import models """

app_config_data="""

# from flask import Flask
# from ..config.config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
#
#
# #Flask project initialization configs
# app=Flask(__name__,template_folder='../templates',static_folder="../static")
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# login = LoginManager(app)
# login.init_app(app)
# login.login_view = 'login'


"""
init_app_config=""" from . import app_config"""

config_data="""
# import os
# basedir = os.path.abspath(os.path.dirname(__file__))
#
#
# class Config(object):
#     DEBUG = False
#     TESTING = False
#     CSRF_ENABLED = True
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
#     SQLALCHEMY_TRACK_MODIFICATIONS=True
#     SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
#
# class ProductionConfig(Config):
#     DEBUG = False
#
#
# class StagingConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True
#
#
# class DevelopmentConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True
#
#
# class TestingConfig(Config):
#     TESTING = True

"""
init_config_data="""from . import config """


controllers_data="""
# from ..app_config.app_config import app,db
# from flask import render_template,request,flash,redirect,url_for
# from werkzeug.urls import url_parse
# from flask_login import current_user, login_user, logout_user,login_required
# from ..forms.forms import LoginForm, RegistrationForm, ContactUs
# from ..models.models import User,Contact_us,Post
#
# @app.route('/')
# @app.route('/index')
# def index():
#     return render_template('index.html',title="Flask App Layout")
#
# @app.route('/About')
# def App_about():
#     return render_template('about.html',title="About Us")
#
# @app.route('/services')
# def App_services():
#     return render_template('services.html',title="Services")
#
# @app.route('/thank_you')
# def App_thank_you_note():
#     return render_template('Thank_you.html',title="Thank You")
#
# #Contact Us
# @app.route('/contact',methods=['GET','POST'])
# def App_contact():
#     form=ContactUs()
#     if form.validate_on_submit():
#         user_comment=Contact_us(name=form.name.data,email=form.email.data,comment=form.comment.data)
#         db.session.add(user_comment)
#         db.session.commit()
#         flash('Comment submited successfully, Thank you!')
#         return redirect(url_for('App_thank_you_note'))
#     else:
#         flash("Fill the form below, we will get back to you asap!")
#         return render_template('contact.html', title='Contact Us', form=form)
#
#
# #login users
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user is None or not user.check_password(form.password.data):
#             flash('Invalid username or password')
#             return redirect(url_for('login'))
#         login_user(user, remember=form.remember_me.data)
#         next_page = request.args.get('next')
#         if not next_page or url_parse(next_page).netloc != '':
#             next_page = url_for('index')
#         return redirect(next_page)
#     return render_template('login.html', title='Sign In', form=form)
#
#
# #logout users
# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))
#
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         user = User(username=form.username.data, email=form.email.data,gender=form.gender.data)
#         user.set_password(form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash('Congratulations, you are now a registered user!')
#         return redirect(url_for('login'))
#     return render_template('register.html', title='Register', form=form)
#
# @app.route('/Blog')
# @login_required
# def Blog():
#     posts={}
#     return render_template('posts.html',title="Blog Posts",user=current_user,posts=posts)

"""
init_controllers_data="""from . import controllers"""

forms_data="""
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
# from wtforms.widgets import TextArea
# from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
# from ..models.models import User,Contact_us
#
# class LoginForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     remember_me = BooleanField('Remember Me')
#     submit = SubmitField('Sign In')
#
#
# class RegistrationForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     gender=SelectField('Gender',choices=[('male','Male'),('female','Female')],validators=[DataRequired()])
#     password = PasswordField('Password', validators=[DataRequired()])
#     password2 = PasswordField('Repeat Password', validators=[DataRequired(),
#                                                              EqualTo('password')])
#     submit = SubmitField('Register')
#
#     def validate_username(self, username):
#         user = User.query.filter_by(username=username.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different username.')
#
#     def validate_email(self, email):
#         user = User.query.filter_by(email=email.data).first()
#         if user is not None:
#             raise ValidationError('Please use a different email address.')
#
# class ContactUs(FlaskForm):
#     name=StringField('Username',validators=[DataRequired()])
#     email=StringField('Email',validators=[DataRequired(),Email()])
#     comment=StringField('Comment',validators=[DataRequired()],widget=TextArea())
#     submit=SubmitField('Submit')


"""
init_forms_data="""from . import forms """


req_data="""
alembic==0.9.9
click==6.7
Flask==1.0.2
Flask-Login==0.4.1
Flask-Migrate==2.1.1
Flask-SQLAlchemy==2.3.2
Flask-WTF==0.14.2
itsdangerous==0.24
Jinja2==2.10
Mako==1.0.7
MarkupSafe==1.0
psycopg2==2.7.4
psycopg2-binary==2.7.4
python-dateutil==2.7.3
python-editor==1.0.3
six==1.11.0
SQLAlchemy==1.2.8
Werkzeug==0.14.1
WTForms==2.2
"""
