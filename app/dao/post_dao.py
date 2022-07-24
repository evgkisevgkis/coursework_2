# Создание DAO для постов

import json


class PostDAO:
    def __init__(self, path):
        """Указание пути к файлу с данными"""
        self.path = path

    def load_posts(self):
        """Загрузка данных из файла"""
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_json(self):
        data = self.load_posts()
        return data

    def search_posts(self, keyword):
        """Поск по вхождению в содержание поста"""
        posts = self.load_posts()
        posts_filtred = []
        for post in posts:
            if keyword in post["content"].lower():
                posts_filtred.append(post)
        return posts_filtred

    def load_post(self, pk):
        """Получить пост по ID"""
        posts = self.load_posts()
        for post in posts:
            if post["pk"] == pk:
                return post

    def user_feed(self, username):
        """Получить все посты пользователя"""
        posts = self.load_posts()
        posts_filtred = []
        for post in posts:
            if username.lower() in post["poster_name"].lower():
                posts_filtred.append(post)
        return posts_filtred
