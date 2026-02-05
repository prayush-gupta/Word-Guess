import os
import pandas as pd
from words_generator import word_generator
from hint_generator import ask_for_hint
from support_functions import get_single_char

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
    try:
      keyword = word_generator()
    except:
      print('Sorry, there was an error[',i,'], please press any key to retry or press q to quit')
      retry_key = get_single_char()
      if retry_key == 'q':
        break
      else:  
        continue
    
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


def play_the_game(keyword, total_guess):
  underscores = '_' * len(keyword)
  guess_counter = 0
  hint_requested = 'no'
  result = ''

  print(underscores)
  print()
  print('You are allowed ',total_guess,' incorrect guesses')
  print()
  print('Press ~ for a hint')
  print()

  while guess_counter < total_guess and underscores != keyword:
    print()
    print('Enter a letter: ')
    guess = get_single_char()
    if guess == '~':
      os.system('clear')
      try:
        hint = ask_for_hint(keyword)
      except:
        hint = 'Sorry, no hint available, try again later'
      hint_requested = 'yes'

    elif guess in keyword:
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
    if hint_requested == 'yes':
      print()
      print('HINT: ', hint)


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


