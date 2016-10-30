from flask import *
from utils import mongo
import uuid

bp = Blueprint(__name__, "post")

def escape(text):
    return text.strip("<").strip(">")

@bp.before_request
def redir():
    if "login" not in session:
        return redirect("/")

@bp.route("/post/")
def returnTemplate():
    return render_template("post.html")

@bp.route("/post/", methods=['POST'])
def postData():
    post_data = escape(request.form['post'][:120])
    username = session['login']
    mongo.db.posts.insert({"username":username, "text":post_data, "reposts":0, "post_id":uuid.uuid4().hex})
    return redirect("/feed/" + username)
