import os
from functions import get_random_fruit_from_api, get_single_char

# fruit = input('Enter a fruit: ')
fruit = get_random_fruit_from_api()
print(fruit)
input('Press enter to continue')
os.system('clear')
underscores = '_' * len(fruit)
print(underscores)
total_guess = 5
print()
print('You are allowed ',total_guess,' incorrect guesses')
print()

guess_counter = 0
while guess_counter < total_guess and underscores != fruit:
  print()
  guess_type = 'l'#input('Would you like to guess the fruit or a letter [f/l]')
  print()
  if guess_type == 'f':
      guess = input('Enter the name of the fruit: ')
      if guess == fruit:
        print()
        print("Congrats you guessed the fruit correctly")
        print()
      else:
        print()
        print('The fruit was ', fruit)
        print()
      break
  elif guess_type == 'l':
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
        result = 'Wrong!'
        guess_counter += 1
      os.system('clear')
      print(underscores)
      print()
      print(result)
      print()
      print('You have ', total_guess - guess_counter,' remaining guesses')




if underscores == fruit:
  print()
  print()
  print("Congrats you guessed the fruit correctly")
else:
  print()
  print()
  print('Sorry, you lost!!')