from flask import Flask, render_template, url_for, redirect, request, session, abort, flash
from flask_mail import Mail, Message
from models import *
import uuid
import os, re

# Flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False
# Flask mail setup
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 465,
    MAIL_USE_TSL = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = os.getenv("EMAIL_ADDRESS"),
    MAIL_PASSWORD = os.getenv("EMAIL_PASS"),
))
mail = Mail(app)


def validateEmail(email, User):
    # checks if email is valid
    validEmail =  bool(re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email))
    # checks if email does not already exist in DB
    alreadyExists = User.emailExists(email)
    if validEmail and not alreadyExists:
        return True
    return False



@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()




@app.route("/")
def home():
    if not session.get('logged_in'):
        return render_template('signup.html')
    else:
        return "Hello there logged in user <a href='logout'>Logout</a>"




@app.route("/signup", methods=["POST"])
def user_signup():
    POST_USERNAME = str(request.form["username"])
    POST_PASSWORD = str(request.form["password"])
    POST_EMAIL = str(request.form["email"])

    # Gets the user class
    User = classes.get("User")
    # validates if user already exists in db and is a valid email address
    if validateEmail(POST_EMAIL, User):
        #crafts an email message to send to the user
        message = Message("Hi, welcome to StandardC. Please verify your email address.",
                sender = os.getenv("EMAIL_ADDRESS"),
                recipients=[POST_EMAIL])
        #sends the message
        mail.send(message)

        # dictionary to build the new User
        kwargs = {"username": POST_USERNAME, "password": POST_PASSWORD, "email": POST_EMAIL, "verified": False}
        new_user = User(**kwargs)
        
        # NEED TO HASH PASSWORD BEFORE SENDING IT TO DB
        new_user.save()
        session["logged_in"] = True
        return home()
    else:
        flash("Incorrect Email")
        return home()




@app.route("/login", methods=["GET", "POST"])
def user_login():
    if request.method == "GET":
        return render_template('login.html')

    if request.method == "POST":
        POST_USERNAME = str(request.form["username"])
        POST_PASSWORD = str(request.form["password"])
        POST_EMAIL = str(request.form["email"])

        if request.form["password"] == "password" and request.form["username"] == "admin":
            session["logged_in"] = True
            return "You are now logged in"
        else:
            flash("wrong password!")
            return home()

@app.route("/logout")
def user_logout():
    session["logged_in"] = False
    return home()



if __name__ == "__main__":
    #setting up env for applicaiton based on inputs
    env_var = {'host': '0.0.0.0', 'port': 5001}
    if os.getenv('APP_HOST'):
        env_var['host'] = os.getenv('APP_HOST')
    if os.getenv('APP_PORT'):
        env_var['port'] = int(os.getenv('APP_PORT'))

    #need to generate a secret key for login session
    app.secret_key = os.urandom(12)
    app.run(host=env_var.get('host'), port=env_var.get('port'), threaded=True)
