# Создание DAO для комментариев

import json


class CommentDAO:
    def __init__(self, path):
        """Указание пути к файлу с комментариями"""
        self.path = path

    def load_comments(self):
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def load_comments_to_post(self, pk):
        comments = self.load_comments()
        post_comments = []
        for comment in comments:
            if comment["post_id"] == pk:
                post_comments.append(comment)
        return post_comments
