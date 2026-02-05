import os
import sys
import pandas as pd
from words_generator import word_generator
from hint_generator import ask_for_hint
from user_interaction import user_interaction
from database import save_game_result, init_db


def game_start():
  init_db()
  print('Welcome to the Word Guessing Game!')

  total_guess = max(5, user_interaction('How many guesses would you like to have? ', 'int', 0))

  game_controller(total_guess)
  

def game_controller(total_guess):

  play = 'yes'
  i = 0
  won = 0
  overall_result = []

  while play == 'yes':
    i += 1
    os.system('clear')
    
    try:
      word_type = user_interaction('What kind of words would you like to guess? [Anything[a]/Fruits[f]] ')
      
    except:
      word_type = 'a'
    
    os.system('clear')
    
    print('Generating a word, please wait...')
    keyword = word_generator(word_type)

    if keyword == 'Generation Error':
      os.system('clear')
      print('Sorry, there was an error generating a word. Please try again later')

      if len(overall_result) > 0:
        break

      sys.exit()

    os.system('clear')

    local_won, hint_requested = play_the_game(keyword, total_guess)
    won += local_won

    save_game_result(
        'Fruit' if word_type == 'f' else 'Anything',
        keyword.upper(),
        'Correct' if local_won == 1 else 'Wrong',
        local_won
    )

    overall_result.append([
        'Fruit' if word_type == 'f' else 'Anything',
        keyword.upper(), 'Correct' if local_won == 1 else 'Wrong', hint_requested, local_won])
    print()
    print('You have won', won, 'out of', i, 'games')
    print()
    
    play = user_interaction('Would you like to play again? (yes/no) ').lower()

  print()
  print()
  
  final_result = pd.DataFrame(overall_result, columns=['Category', 'Keyword', 'Result', 'Hint', 'Points'])
  
  final_result['Total Score'] = final_result['Points'].cumsum()
  print(final_result)


def play_the_game(keyword, total_guess):
  underscores = '_' * len(keyword)
  hint_requested = 'no'
  guess_counter = 0
  result = ''

  print(underscores)
  print()
  print('You are allowed ', total_guess, ' incorrect guesses')
  print()
  print('Press ~ for a hint')
  print()

  while guess_counter < total_guess and underscores != keyword:
    print()

    guess = user_interaction('Enter a letter: ', 'string', 1)
    
    if guess == '~':
      os.system('clear')
      try:
        hint = ask_for_hint(keyword)
        hint_requested = 'yes'
      except:
        hint = 'Sorry, no hint available. Please try again later'

    elif guess in keyword:
      replacement_counter = 0
      while replacement_counter < len(keyword):
        if keyword[replacement_counter] == guess:
          underscores = underscores[:replacement_counter] + guess + underscores[
              replacement_counter + 1:]
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
    print('You have ', total_guess - guess_counter, ' remaining guesses')
    if hint_requested == 'yes':
      print()
      print('HINT: ', hint)

  if underscores == keyword:
    result = 1
    print()
    print()
    print("CONGRATS!! You guessed the word", keyword.upper(), "correctly")
  else:
    result = 0
    print()
    print()
    print('Sorry, you lost!!')
    print('The word was ', keyword.upper())
  return result, hint_requested
