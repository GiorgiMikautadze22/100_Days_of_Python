from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Email, Length, email
from flask_bootstrap import Bootstrap5
from werkzeug import security
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
Bootstrap5(app)
app.config['SECRET_KEY'] = 'secret-key-goes-here'


# CREATE DATABASE


class Base(DeclarativeBase):
    pass

class AddUser(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email = EmailField(label="Email", validators=[Email()])
    password = PasswordField(label="Password")
    submit = SubmitField(label="Register")

class LogIn(FlaskForm):
    email = EmailField(label="Email", validators=[Email()])
    password = PasswordField(label="Password")
    submit = SubmitField(label="Log In")


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


# Configure Flask-Login's Login Manager
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = AddUser()

    if form.validate_on_submit():
        user = User(
            email=form.email.data,
            password=security.generate_password_hash(password=form.password.data, method='scrypt', salt_length=8),
            name=form.name.data
        )
        db.session.add(user)
        db.session.commit()
        flash('User has been created')
        return redirect(url_for('secrets'))
    return render_template("register.html", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():

    form = LogIn()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        if check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('secrets'))

    return render_template("login.html", form=form)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path="files/cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True, port=8080)
