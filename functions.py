import requests
import os
import random
import sys
import tty
import termios

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


def play_the_game(fruit):
  total_guess = 5
  underscores = '_' * len(fruit)
  guess_counter = 0

  print(underscores)
  print()
  print('You are allowed ',total_guess,' incorrect guesses')
  print()

  while guess_counter < total_guess and underscores != fruit:
    print()
    print('Enter a letter: ')
    guess = get_single_char()
    if guess in fruit:
      replacement_counter = 0
      while replacement_counter < len(fruit):
        if fruit[replacement_counter] == guess:
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


  if underscores == fruit:
    result = 1
    print()
    print()
    print("CONGRATS!! You guessed the fruit", fruit.upper(),"correctly")
  else:
    result = 0
    print()
    print()
    print('Sorry, you lost!!')
    print('The fruit was ', fruit.upper())
  return result