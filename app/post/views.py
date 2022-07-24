from flask import Blueprint, render_template

from app.dao.post_dao import PostDAO
from app.dao.comment_dao import CommentDAO


# Создаем блупринт
post_blueprint = Blueprint('post_blueprint', __name__, template_folder="templates")

# Создаем DAO
post_dao = PostDAO("./data/data.json")
comment_dao = CommentDAO("./data/comments.json")


# Создаем вьюшку для показа всех постов
@post_blueprint.route('/post/<int:pk>')
def post_page(pk):
    post = post_dao.load_post(pk)
    comments = comment_dao.load_comments_to_post(pk)
    comments_count = len(comments)
    return render_template("post.html", post=post, comments=comments, comments_count=comments_count)
