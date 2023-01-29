import pytest
import json

from app.api.views import api_posts, api_post_id

with open("../../data/data.json", "r", encoding="utf-8") as file:
    data = json.load(file)


class TestApi:
    def test_1(self):
        assert type(api_posts) == list, 'Тип данных - не словарь'

    def test_2(self):
        temp = api_posts
        for i in temp:
            if i.keys in data.keys:
                continue
            else:
                pytest.raises()


class TestApiPost:
    def test_1(self):
        assert type(api_post_id) == list, 'Тип данных - не словарь'

    def test_2(self):
        temp = api_post_id
        for i in temp:
            if i.keys in data.keys:
                continue
            else:
                pytest.raises()
