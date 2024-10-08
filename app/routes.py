from flask import render_template, url_for, flash, redirect
from app import app, db, bcrypt
from app.models import User, Ticket
from app.forms import RegistrationForm, LoginForm

tickets = [
    {
        'owner': 'John Doe',
        'category': 'Cat A',
        'description': 'Hardware trouble',
        'urgent': 'True',
        'created_dt': 'Today'
    },
    {
        'owner': 'Mary Jane',
        'category': 'Cat B',
        'description': 'Software issues',
        'urgent': 'False',
        'created_dt': 'Yesterday'
    },
    {
        'owner': 'Luis Messi',
        'category': 'Cat C',
        'description': 'Database Inadequacies',
        'urgent': 'True',
        'created_dt': 'Today'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', tickets=tickets, title='Home')

@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Log in successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login failed. Invalid credentials', 'danger')
    return render_template('login.html', title='Login', form=form)