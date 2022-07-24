from flask import Flask

from app.main.views import posts_blueprint
from app.post.views import post_blueprint
from app.search.views import search_blueprint
from app.feed.views import user_feed_blueprint
from app.api.views import api_all, api_one

app = Flask(__name__)

app.register_blueprint(posts_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_feed_blueprint)
app.register_blueprint(api_all)
app.register_blueprint(api_one)

if __name__ == "__main__":
    app.run()
