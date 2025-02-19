import json

import requests
from fastjsonschema import validate

from resource import path

url = 'https://reqres.in/api/users'


def test_list_users():
    responce = requests.get(url, params={'page': 2})
    schema = path('list_users.json')
    body = responce.json()

    assert responce.status_code == 200
    with open(schema) as file:
        validate_data = json.loads(file.read())
        validate(body, validate_data)


def test_negative_return_non_existent_id():
    responce = requests.get(url, params={'page': 2, 'id': 100})

    assert responce.status_code == 404
