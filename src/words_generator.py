import requests
import random


def get_random_fruit_from_api():
  # Fetch all fruits from the Fruityvice API
  response = requests.get("https://www.fruityvice.com/api/fruit/all")

  # Check if the request was successful
  if response.status_code == 200:
      fruits_data = response.json()
      # Select a random fruit from the list of fruits
      random_fruit = random.choice(fruits_data)
      return random_fruit["name"]
  else:
      return "Failed to fetch fruits from API"



def get_random_words(count, diff=None, length=None):
    url = f"https://random-word-api.herokuapp.com/word?number={count}"
    if length:
        url += f"&length={length}"

    if diff:
        url += f"&diff={diff}"

    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"


def word_generator():
  os.system('clear')
  try:
    word_type = input('What kind of words would you like to guess? [Anything[a]/Fruits[f]]')
  except:
    word_type = 'a'

  if word_type == 'f':
    keyword = get_random_fruit_from_api().lower()
  else:
    keyword = get_random_words(1, diff = 2, length = random.randrange(6,15))[0].lower()
  return keyword