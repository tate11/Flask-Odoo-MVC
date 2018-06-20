Basic Flask Shell Commands
------------------------------------
------------------------------------

Flask Commands
-------------------------------------
(+) Flask run --> runs a flask project
(+) Flask shell --> starts an instance of python shell in relation to the project.

Environment Variables
-------------------------------------
export FLASK_APP=name_of_app.py --> tells flask how to import and run project.
export FLASK_DEBUG=True or False --> this enbles debug mode.
export FLASK_ENV=development ---> this enables debug mode.
export DATABASE_URL='postgresql://flask:12345@localhost:5432/blog' url path to your database.


Database Management
-------------------------------------------
flask db init ---> intialize migrations.
flask db migrate -m "users table" --->create table.
flask upgrade  ---> upgrade or commit to db.
flask downgrade ---> down grade to previous commit.

Flask Shell database Tests
-------------------------------------------
You will notice that main_app.py has _@app.shell_context_processor_
to aid in loading a dictionary of "_modules_" to be use in the shell_
session.

Multiple changes can be accumulated in a session and once all the
changes have been registered you can issue a single _db.session.commit()_,
which writes all the changes atomically. If at any time while working on
a session there is an error, a call to _db.session.rollback()_ will abort
the session and remove any changes stored in it. The important thing to
remember is that changes are only written to the database when
_db.session.commit()_ is called. Sessions guarantee that the database
will never be left in an inconsistent state.

(+) Start a flask shell session "_flask shell_"

Do the below:
    >>> db
    <SQLAlchemy engine=postgresql://fUser:***@localhost:5432/flask>

    >>> u=User(username="Paul",email="paul@gmail.com")
    >>> db.session.add(u)
    >>> db.session.commit()
    >>> p=User(username="Mary",email="mary@gmail.com")
    >>> db.session.add(p)
    >>> db.session.commit()
    >>> users=User.query.all()
    >>> users
    [<User Paul>, <User Mary>]
    >>>
