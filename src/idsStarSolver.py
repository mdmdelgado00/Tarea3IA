from gamebuilder import get_children, manhattan_distance
import math

# Goal board
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# IdsStar main function solver
def IdsStarSolver(board):
    threshold = manhattan_distance(board)
    while True:
        result = limitedDepthSearch(board, 0, threshold)
        # If the goal is found
        if isinstance(result, list):
            return result
        # If there is no solution
        if result == math.inf:
            return None
        threshold = result

# Depth search limited by threshold
def limitedDepthSearch(board, g, threshold):
    f = g + manhattan_distance(board)
    if f > threshold:
        return f
    if board == goal:
        return [board]
    
    min = math.inf
    for nextState in get_children(board):
        result = limitedDepthSearch(nextState, g + 1, threshold)
        if isinstance(result, list):  # Si encontramos el camino
            return [board] + result
        if result < min:
            min = result
    return min
