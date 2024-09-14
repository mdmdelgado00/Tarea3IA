from gamebuilder import get_children

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def depthSearch(board, depth):
  # If the solution was found
  if board == goal:
    return board
  
  # If the solution was not found
  if depth == 0:
    return None

  # Search each child until the specified depth
  for child in get_children(board):
    result = depthSearch(child, depth - 1)
    # If the solution was found in a child
    if result is not None:
      return result

  # If the solution was not found in a child
  return None


def IdsSolver(board):
  depth = 0

  # Search increasing the depth in each iteration
  while True:
    result = depthSearch(board, depth)
    # If the solution was not found
    if result is not None:
      return result
    depth += 1