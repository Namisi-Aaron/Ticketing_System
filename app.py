from crypt import methods
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '2d23334fbbba726538a323b866fdbfd0'

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
        flash('Account created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('home'))
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

if __name__ == "__main__":
    app.run(debug=True)