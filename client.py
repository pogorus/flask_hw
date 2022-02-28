import requests

HOST = 'http://127.0.0.1:8000'

response = requests.post(f'{HOST}/ad', json={
    'title': 'title_1',
    'description': 'description_1',
    'owner': 'owner_1'
})
print(response.status_code)
print(response.text)

response = requests.get(f'{HOST}/ad/1')
print(response.status_code)
print(response.text)

response = requests.patch(f'{HOST}/ad/1', json={
    'title': 'title_10',
    'description': 'description_10',
    'owner': 'owner_10'
})
print(response.status_code)
print(response.text)

response = requests.delete(f'{HOST}/ad/1')
print(response.status_code)
print(response.text)
