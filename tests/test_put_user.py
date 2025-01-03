import requests

from resource import path
from fastjsonschema import validate
import json

url = 'https://reqres.in/api/users/2'
name = 'Nikita'
job = 'Doctor'


def test_update_user_name_and_job():
    new_user_id = requests.post(url, data={'name': 'Vanya', 'job': 'translator'}).json()['id']
    responce = requests.put(f'https://reqres.in/api/users/{new_user_id}', json={'name': name, 'job': job})
    body = responce.json()
    schema = path('put_user.json')

    assert responce.status_code == 200
    assert body['name'] == name
    assert body['job'] == job
    with open(schema) as file:
        validate_data = json.loads(file.read())
        validate(validate_data, body)
