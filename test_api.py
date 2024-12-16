import requests

# api_url = 'http://127.0.0.1:8000/api/convert/'
api_url = 'https://79c3-84-54-83-43.ngrok-free.app/api/convert/'
data = {
    'number': 15
}
response = requests.post(api_url, json=data)
print(response.text)
