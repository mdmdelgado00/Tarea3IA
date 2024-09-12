from gamebuilder import get_children
import time
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def BfsSolver(board):
  states = 0
  queue = []
  visited = []
  queue.append(board)
  while queue:
    current = queue.pop(0)
    states += 1
    print(states)
    if current == goal:
      print("Goal found")
      return
    if current in visited:
      continue
    visited.append(current)
    queue.extend(get_children(current))




