import requests

from resource import path
from fastjsonschema import validate
import json

url = 'https://reqres.in/api/users'
payload = {'name': 'Misha', 'job': 'developer'}


def test_schema_validate_from_file():
    responce = requests.post(url, data=payload)
    schema = path('user.json')
    body = responce.json()

    assert responce.status_code == 201
    with open(schema) as file:
        validate_data = json.loads(file.read())
    validate(body, validate_data)
