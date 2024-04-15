def is_first_of_the_month(day_number):
  if day_number == 1:
    return 'First of the month!'
  else: 
    return 'Not first of the month'
  

def has_five_chars(the_str):
  if len(the_str) == 5: 
    return f'{the_str} is five characters long'
  else:
    return 'Not five characters'