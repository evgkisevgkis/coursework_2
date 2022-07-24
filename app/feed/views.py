from flask import Blueprint, render_template

from app.dao.post_dao import PostDAO
from app.dao.comment_dao import CommentDAO


# Создаем блупринт
user_feed_blueprint = Blueprint('user_feed_blueprint', __name__, template_folder="templates")

# Создаем DAO
post_dao = PostDAO("./data/data.json")
comment_dao = CommentDAO("./data/comments.json")


# Создаем вьюшку для показа всех постов
@user_feed_blueprint.route('/user/<poster_name>')
def user_feed_page(poster_name):
    posts = post_dao.user_feed(poster_name)
    return render_template("user-feed.html", posts=posts)
