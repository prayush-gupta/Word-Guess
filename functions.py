import requests
import os
import random
import sys
import tty
import termios
import pandas as pd

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


def get_single_char():
  """Reads a single character from tty without Enter."""
  fd = sys.stdin.fileno()
  old_settings = termios.tcgetattr(fd)
  try:
      tty.setraw(sys.stdin.fileno()) # Set to raw mode
      ch = sys.stdin.read(1)        # Read exactly 1 char
  finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) # Reset
  return ch


def cels_to_fahr():
    while True:
        try:
            celsius = float(input('Please enter the temperature in Celsius: '))
            break
        except:
            print('You did not enter a valid number, try again')
    fahrenheit = (celsius * (9/5)) + 32
    print('The temperature in Fahrenheit is: ', fahrenheit)


def play_the_game(keyword, total_guess):
  underscores = '_' * len(keyword)
  guess_counter = 0

  print(underscores)
  print()
  print('You are allowed ',total_guess,' incorrect guesses')
  print()

  while guess_counter < total_guess and underscores != keyword:
    print()
    print('Enter a letter: ')
    guess = get_single_char()
    if guess in keyword:
      replacement_counter = 0
      while replacement_counter < len(keyword):
        if keyword[replacement_counter] == guess:
          underscores = underscores[:replacement_counter] + guess + underscores[replacement_counter+1:]
        replacement_counter += 1
      result = 'You guessed a letter correctly'
    else:
      result = 'Wrong guess!'
      guess_counter += 1
    os.system('clear')
    print(underscores)
    print()
    print(result)
    print()
    print('You have ', total_guess - guess_counter,' remaining guesses')


  if underscores == keyword:
    result = 1
    print()
    print()
    print("CONGRATS!! You guessed the word", keyword.upper(),"correctly")
  else:
    result = 0
    print()
    print()
    print('Sorry, you lost!!')
    print('The word was ', keyword.upper())
  return result


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


def game_controller():
    try:
      total_guess = max(5, int(input('How many guesses would you like to have?')))
    except:
      total_guess = 5
  
    play = 'yes'
    i = 0
    won = 0
    overall_result = []

    while play == 'yes':
      i += 1
      os.system('clear')
      try:
        word_type = input('What kind of words would you like to guess? [Anything[a]/Fruits[f]]')
      except:
        word_type = 'a'

      if word_type == 'f':
        keyword = get_random_fruit_from_api().lower()
      else:
        keyword = get_random_words(1, diff = 2, length = random.randrange(6,15))[0].lower()
      
      local_won = play_the_game(keyword, total_guess)
      won += local_won

      overall_result.append(['Fruit' if word_type == 'f' else 'Anything', keyword.upper(), 'Correct' if local_won == 1 else 'Wrong', local_won])
      print()
      print('You have won', won, 'out of', i,'games')
      print()
      play = input('Would you like to play again? (yes/no) ').lower()

    print()
    print()
    final_result = pd.DataFrame(overall_result, columns=['Category', 'Keyword', 'Result', 'Points'])
    final_result['Total Score'] = final_result['Points'].cumsum()
    print(final_result)
    return final_result
