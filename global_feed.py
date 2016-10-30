from flask import *
from utils import mongo

bp = Blueprint(__name__, "live")

@bp.route("/")
def globalFeed():
    return render_template("global.html", feed=mongo.db.posts.find().sort("_id", -1).limit(25))
