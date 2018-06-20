from ..app_config.app_config import app,db
from flask import render_template,request,flash,redirect,url_for
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user,login_required
from ..forms.forms import LoginForm, RegistrationForm, ContactUs
from ..models.models import User,Contact_us,Post

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title="Flask App Layout")

@app.route('/About')
def App_about():
    return render_template('about.html',title="About Us")

@app.route('/services')
def App_services():
    return render_template('services.html',title="Services")

@app.route('/thank_you')
def App_thank_you_note():
    return render_template('Thank_you.html',title="Thank You")

#Contact Us
@app.route('/contact',methods=['GET','POST'])
def App_contact():
    form=ContactUs()
    if form.validate_on_submit():
        user_comment=Contact_us(name=form.name.data,email=form.email.data,comment=form.comment.data)
        db.session.add(user_comment)
        db.session.commit()
        flash('Comment submited successfully, Thank you!')
        return redirect(url_for('App_thank_you_note'))
    else:
        flash("Fill the form below, we will get back to you asap!")
        return render_template('contact.html', title='Contact Us', form=form)


#login users
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


#logout users
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,gender=form.gender.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/Blog')
@login_required
def Blog():
    posts={}
    return render_template('posts.html',title="Blog Posts",user=current_user,posts=posts)
