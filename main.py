import functions
import os
import pandas as pd

play = 'yes'
i = 0
won = 0
overall_result = []
overall_result.append(['Fruit','Result'])

while play == 'yes':
  i += 1
  os.system('clear')
  fruit = functions.get_random_fruit_from_api().lower()
  local_won = functions.play_the_game(fruit)
  won += local_won 
  overall_result.append([fruit, local_won])
  print()
  print('You have won', won, 'out of', i,'games')
  print()
  play = input('Would you like to play again? (yes/no) ').lower()

print()
print()
print(pd.DataFrame(overall_result, columns=['Fruit', 'Result']))

# print(functions.get_random_fruit_from_api())