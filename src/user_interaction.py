from support_functions import get_single_char


def user_interaction(message, entry_type = 'string', single_entry = 0):
  
  if single_entry == 1:
    user_entry = get_single_char()
  
  else:
    user_entry = input(message)
    
  if entry_type == 'int':
    try:
      return int(user_entry)
    except:
      return -1

  return user_entry