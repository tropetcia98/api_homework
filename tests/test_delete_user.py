import requests

url = 'https://reqres.in/api/users/2'


def test_delete_user():
    new_user_id = requests.post(url, data={'name': 'Vanya', 'job': 'translator'}).json()['id']
    responce = requests.delete(f'https://reqres.in/api/users{new_user_id}')

    assert responce.status_code == 204
