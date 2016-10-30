from flask import *
from utils import mongo
from hashlib import sha512

bp = Blueprint(__name__, "authenticate")

@bp.route("/logout/")
def logout():
    session.pop("login")
    return redirect("/")

@bp.route("/login/")
def returnTemplate():
    return render_template("login.html")

@bp.route("/login/", methods=['POST'])
def login_post():
    username = escape(request.form['username'])
    password = request.form['password']
    if mongo.db.members.find_one({"username":username, "password":sha512(password).hexdigest()}):
        session["login"] = username
        return redirect("/feed/" + username)
    else:
        return "Login Failed"

@bp.route("/register/")
def returnRegTemp():
    return render_template("register.html")

@bp.route("/register/", methods=['POST'])
def register_post():
    username = escape(request.form['username'])
    password = request.form['password']
    confirm = request.form['confirm']
    check = mongo.db.members.find_one({"username":username})
    if not check and password == confirm:
        mongo.db.members.insert({"username":username, "password":sha512(password).hexdigest()})
        session['login'] = username
        return redirect("/feed/" + username)
    else:
        return "Registration Failed"
