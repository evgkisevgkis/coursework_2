from flask import Blueprint, render_template

from app.dao.post_dao import PostDAO


# Создаем блупринт
posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder="templates")

# Создаем DAO
post_dao = PostDAO("./data/data.json")


# Создаем вьюшку для показа всех постов
@posts_blueprint.route('/')
def main_page():
    posts = post_dao.load_posts()
    return render_template("index.html", posts=posts)
