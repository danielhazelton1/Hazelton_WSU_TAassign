from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from app.models import Courses
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app import db
from app.forms import RegistrationForm
from app.forms import EditForm
from app.forms import AddForm

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title='Home Page', posts=posts)

@app.route('/student')
@login_required
def student():	
	return render_template("student.html", title='Student_page')

@app.route('/instructor', methods=['GET', 'POST'])
@login_required
def instructor():
	course = Courses.query.all()
	return render_template("instructor.html", title='Instructor_page', course = course )
	
@app.route('/edit_instructor', methods=['GET', 'POST'])
@login_required
def edit_instructor():	
	form = EditForm()
	if form.validate_on_submit():
		user = current_user
		# user = User(name=form.name.data, lastname=form.lastname.data, wsuID=form.wsuID.data,phone=form.phone.data)
		user.name=form.name.data
		user.lastname=form.lastname.data
		user.wsuID=form.wsuID.data
		user.phone=form.phone.data
		db.session.commit()
		return redirect(url_for('instructor'))
	
	return render_template("edit_instructor.html", title='Instructor_edit_page', form=form)

@app.route('/edit_student', methods=['GET', 'POST'])
@login_required
def edit_student():	
	form = EditForm()
	if form.validate_on_submit():
		user = current_user
		# user = User(name=form.name.data, lastname=form.lastname.data, wsuID=form.wsuID.data,phone=form.phone.data)
		user.name=form.name.data
		user.lastname=form.lastname.data
		user.wsuID=form.wsuID.data
		user.phone=form.phone.data
		db.session.commit()
		return redirect(url_for('student'))
	return render_template("edit_student.html", title='edit_Student_page', form=form)
@app.route('/addcourse', methods=['GET', 'POST'])
@login_required
def addcourse():	
	form = AddForm()
	if form.validate_on_submit():
		course = Courses(name=form.name.data)
		db.session.add(course)
		db.session.commit()
		return redirect(url_for('instructor'))
	return render_template("addcourse.html", title='addcourses_page', form=form)
	
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data) or form.type.data != user.type:
            flash('Invalid username, password, or role')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        if user.type == "student":
            return redirect(url_for('student'))
        if user.type == "instructor":
            return redirect(url_for('instructor'))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
	
    # if form.validate_on_submit():
        # user = User.query.filter_by(username=form.username.data).first()
        # if user is None or not user.check_password(form.password.data):
            # flash('Invalid username or password')
            # return redirect(url_for('login'))
        # login_user(user, remember=form.remember_me.data)
        # next_page = request.args.get('next')
        # if not next_page or url_parse(next_page).netloc != '':
            # next_page = url_for('index')
        # return redirect(next_page)
		
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
        #user = User(username=form.username.data, email=form.email.data)
        user = User(username=form.username.data, email=form.email.data, type=form.type.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)