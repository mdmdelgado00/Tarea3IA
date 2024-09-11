from random import randrange 

def build_gameboard():
  matrix = []
  numbers = list(range(1, 9))
  numbers.append(None)
  for i in range(3):
    row = []
    for j in range(3):
      while True:
        number = numbers.pop(randrange(len(numbers)))
        row.append(number)
        break
    matrix.append(row)
  return matrix


  