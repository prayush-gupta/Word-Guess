import os
import requests
import random
import sys
import tty
import termios

print("Executed")

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
