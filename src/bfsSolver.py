from gamebuilder import get_children
from collections import deque
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def BfsSolver(board):
  queue = deque()
  visited = set()
  queue.append(board)
  # Se convierte a tupla para poder meterlo en el set
  start_tuple = tuple(tuple(row) for row in board)
  visited.add(start_tuple)
  while queue:
    current = queue.popleft()
    # Se convierte a tupla para poder meterlo en el set
    current_tuple = tuple(tuple(row) for row in current)
    visited.add(current_tuple)
    
    if current == goal:
      print("Goal found")
      return
    
    for child in get_children(current):
      child_tuple = tuple(tuple(row) for row in child)
      if child_tuple not in visited:
        queue.append(child)
