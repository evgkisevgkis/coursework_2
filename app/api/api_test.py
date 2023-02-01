import pytest
import json

from app.api.views import api_posts, api_post_id

with open("./data/data.json", "r", encoding="utf-8") as file:
    data = json.load(file)


class TestApi:
    def test_1(self):
        assert type(api_posts()) == list, 'Тип данных - не список'

    def test_2(self):
        assert api_posts() == data, 'Ошибка в соединении с файлом'


class TestApiPost:
    @pytest.mark.parametrize(
        'test_input, expected',
        [(1, dict), (2, dict), (3, dict), (4, dict), (5, dict), (6, dict), (7, dict), (8, dict)]
    )
    def test_1(self, test_input, expected):
        assert type(api_post_id(int(test_input))) == expected, 'Тип данных - не словарь'

    @pytest.mark.parametrize(
        'test_input, expected',
        [(1, data[0].keys()), (2, data[1].keys()), (3, data[2].keys()), (4, data[3].keys()), (5, data[4].keys()),
         (6, data[5].keys()), (7, data[6].keys()), (8, data[7].keys())]
    )
    def test_2(self, test_input, expected):
        assert api_post_id(int(test_input)).keys() == expected, 'Тип данных - не словарь'
