from flask import *
import authenticate, post, feed, global_feed

app = Flask(__name__)
app.jinja_env.autoescape = False
app.secret_key = "sadas123123asd"

app.register_blueprint(authenticate.bp)
app.register_blueprint(post.bp)
app.register_blueprint(feed.bp)
app.register_blueprint(global_feed.bp)

if __name__ == "__main__":
    app.run(debug=True)
