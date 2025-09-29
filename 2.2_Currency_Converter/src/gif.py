import requests
import os

url = 'https://api.giphy.com/v1/gifs/trending'

api_key = 'UwJC8N6AYpgElmgjqoMePjoFGNSlH702'

params = {
    'api_key': api_key,
    'limit': 10
}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    for item in data['data']:
        print(f"name: {item['title']}\nLink: {item['url']}")
        print('-'*100)
else:
    print('error during fetch data')
