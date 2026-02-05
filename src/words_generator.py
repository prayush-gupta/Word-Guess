import requests
import random
from support_functions import get_single_char
import re


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
    print(response)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"


def word_generator(word_type):

    generation_try = 0

    while generation_try < 3:

        if generation_try > 0:
            print('Retrying to generate a word, please wait...')
        
        if word_type == 'f':
            try:
                keyword = get_random_fruit_from_api().lower()
                break
            except:
                generation_try += 1
                continue
        else:
            keyword = get_random_words(1, diff = 2, length = random.randrange(6,15))
            if re.search('^Error:', keyword):
                
                print('Sorry, there was an error[',keyword,'], please press any key to retry or press q to quit')
                keyword = 'Generation Error'
                
                retry_key = get_single_char()
                if retry_key == 'q':
                    break
                else:
                    generation_try += 1
                    continue
                
            else:
                keyword = keyword[0].lower()

    return keyword