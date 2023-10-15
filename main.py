def make_rails(message, num_of_rails):
  ''' 
  @param message is a string to be encrpyted
  print a list of indeces indicating which rail each letter in the message should be placed on
  '''
  # Initializing the variables:
  rail_position = -1
  Down = True
  Up = False
  rail_num_indeces = []

  # Processing during conditions:
  for indeces in range(0, len(message)): #For loop to do 14 iterations because rail_num_indeces will store 14 values indicating placement of letters
    if Down: # if Down is True, rail_position will be incremented by 1 and added to the list until otherwise False
      rail_position += 1
      rail_num_indeces.append(rail_position)
      if rail_position == num_of_rails - 1: # if rail_position == num_of_rails - 1, Down = False and Up = True will execute to indicate if Down is false in the following iteration
        Down = False
        Up = True
    elif Up: # if rail_position == num_of_rails - 1, elif Up will execute and rail_position will decrement by 1 and added to the list until otherwise False
      rail_position -= 1
      rail_num_indeces.append(rail_position)
      if rail_position == 0: # if rail_position == 0, Down = True and Up = False will execute to indicate elif Up is False in the following iteration
        Down = True
        Up = False

  return rail_num_indeces # Returns list of indeces following the 14th iteration

def encrypt_rail_fence(message, num_rails):
  rails = []
  for i in range(num_rails):
    rails.append([])
  Down = True
  Up = False
  rail_position = 0
  for letter in message:
    if letter == " ":
      pass
    else:
      rails[rail_position].append(letter)
      if Down:
        rail_position += 1
        if rail_position == num_rails - 1:
          Down = False
          Up = True
      elif Up: 
        rail_position -= 1
        if rail_position == 0: 
          Down = True
          Up = False
  result = ''
  for list in rails:
    for string in list:
      result += string
    result += " " # adds the spaces (talk about in video)
  return result.strip() #closes the final space (talk about in video)
  
print(encrypt_rail_fence("WEATHER IS QUITE NICE TODAY", 3))

def decrypt_rail_fence(message, num_rails):
  rails = []
  for i in range(num_rails):
    rails.append([])
  Down = True
  Up = False
  rail_position = 0
  for letter in message:
      if letter != " ":
          rails[rail_position].append(letter)
      if Down:
        if letter == " ":
            rail_position += 1
            Down = False
            Up = True
      elif Up: 
        if letter == " ": 
            rail_position += 1
            Down = True
            Up = False
  result = ''
  rail_position = 0
  Down = True
  Up = False
  for letters in message:
    if len(rails[rail_position]) == 0:
      break
    else:
      result += rails[rail_position][0]
      rails[rail_position].pop(0)
      if Down:
        rail_position += 1
        if rail_position == num_rails - 1:
          Down = False
          Up = True
      elif Up:
        rail_position -= 1
        if rail_position == 0:
          Down = True
          Up = False
  return result
  
print(decrypt_rail_fence("POIEM SLTHSPRTE SLHTIUSESE TEEESSERSG HRACA", 5))