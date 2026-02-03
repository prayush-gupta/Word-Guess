#print('Hello world - main')

# import hello

import requests

url = "https://random-word-api.herokuapp.com/word"
response = requests.get(url)

if response.status_code == 200:
    words = response.json()
    print(f"Random word: {words[0]}")
else:
    print(f"Error: {response.status_code}")