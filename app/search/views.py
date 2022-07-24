from flask import Blueprint, render_template, request

from app.dao.post_dao import PostDAO
from app.dao.comment_dao import CommentDAO


# Создаем блупринт
search_blueprint = Blueprint('search_blueprint', __name__, template_folder="templates")

# Создаем DAO
post_dao = PostDAO("./data/data.json")
comment_dao = CommentDAO("./data/comments.json")


# Создаем вьюшку для показа всех постов
@search_blueprint.route('/search')
def search_posts():
    s = request.args.get('s')
    posts_filtred = post_dao.search_posts(s)
    posts_ammount = len(posts_filtred)
    return render_template("search.html", posts=posts_filtred, posts_ammount=posts_ammount)
