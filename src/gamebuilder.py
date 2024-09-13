from random import randrange 

def build_gameboard():
  matrix = []
  numbers = list(range(0, 9))
  for i in range(3):
    row = []
    for j in range(3):
      while True:
        number = numbers.pop(randrange(len(numbers)))
        row.append(number)
        break
    matrix.append(row)
  return matrix

def get_children(board):
  children = []
  x, y = get_zero(board)
  if x > 0:
    new_board = [row[:] for row in board]
    new_board[x][y], new_board[x - 1][y] = new_board[x - 1][y], new_board[x][y]
    children.append(new_board)
  if x < 2:
    new_board = [row[:] for row in board]
    new_board[x][y], new_board[x + 1][y] = new_board[x + 1][y], new_board[x][y]
    children.append(new_board)
  if y > 0:
    new_board = [row[:] for row in board]
    new_board[x][y], new_board[x][y - 1] = new_board[x][y - 1], new_board[x][y]
    children.append(new_board)
  if y < 2:
    new_board = [row[:] for row in board]
    new_board[x][y], new_board[x][y + 1] = new_board[x][y + 1], new_board[x][y]
    children.append(new_board)
  return children

def get_zero(board):
  for i in range(3):
    for j in range(3):
      if board[i][j] == 0:
        return i, j
  return -1, -1
