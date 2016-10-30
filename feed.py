from flask import *
from utils import mongo

bp = Blueprint(__name__, "feed")

@bp.route("/feed/<username>")
def feed(username):
    posts = mongo.db.posts.find({"username":username}).sort("_id", -1).limit(25)
    return render_template("feed.html", feed=posts)

@bp.route("/feed/", methods=['POST'])
def repost():
    if "login" not in session:
        return redirect("/login/")
    post_id = request.form['post_id']
    check = mongo.db.posts.find_one({"post_id":post_id})
    if check:
        if not mongo.db.posts.find_one({"post_id":post_id, "username":session['login']}):
            mongo.db.posts.update({"post_id":post_id}, {"$set":{"reposts":check['reposts'] + 1}})
            mongo.db.posts.insert({"post_id":post_id, "username":session['login'], "reposts":check['reposts'] + 1, "text":check['text']})
        return "Great"
    return "Invalid post id"

