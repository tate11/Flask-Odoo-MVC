

#  **Flask Project Folder Structure v1.0**
            

This repo is a demonstration of how one can structure Flask projects. It is
a fork of Odoo's module structure, thus might relate well with Odoo users
interested in flask. Its not a standard flask project structure, but a reflection
of how it can be done among many other concepts out there. This is version 1.0 hopefully
others will improve on it, patch it etc.


Below is the structure, better viewed in an editor e.g _atom_:


#   **Package Structure**


* **uploads** _(optional)_

* **Tools**  _(optional)_

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






# **Definitions**


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

  (+) **Tools**
  ---------------------------------------------------------------------
  Contains a script utility _flask-odoo-MVC.py_ used to generate the project
  structure above. Its more like _scaffold_ in Odoo. How to use it:

      * _python3 flask-odoo-MVC.py path_of_project_

  **NB**  
  -------------------------------------------------
  * Before using this project Structure, make sure all requirements have been installed.
          * packages in requirements.txt
          * editior, IDE esp _atom_ really cool ;-)
          * etc

  * Understand python2 and python3, esp _python3_
  * Be familiar with Odoo MVC.
  * Be a beginner or intermediate dev of _flask_.
  * Understand how python structures and accesses _modules_ and _packages_






#      **Major Requirements**

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
  * (+) ./run_app.sh    (i.e _Below are the values to enter when running the shell script._)
              *   main_app.py
              *   development
              *   True
