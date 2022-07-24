from flask import Blueprint
import logging
from app.dao.post_dao import PostDAO


# Создаем блупринты
api_all = Blueprint('api_all', __name__, template_folder="templates")
api_one = Blueprint('api_one', __name__, template_folder="templates")

# Создаем DAO
post_dao = PostDAO("../../data/data.json")


# Создаем эндпоинты, которые возвращают данные в формате JSON
@api_all.route('/api/posts/')
def api_posts():
    """Возвращает все посты в формате JSON"""
    posts = post_dao.get_json()
    logging.info('Запрошены все посты')  # Логгирование запроса всех постов
    return posts


@api_one.route('/api/posts/<int:post_id>')
def api_post_id(post_id):
    """Возвращает конкретный пост в JSON"""
    post = post_dao.load_post(post_id)
    logging.info(f'Запрошен пост №{post_id}')  # Логгирование запроса одного поста
    return post
