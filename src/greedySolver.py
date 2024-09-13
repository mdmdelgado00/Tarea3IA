import heapq
from gamebuilder import get_children

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Heurística de Manhattan
def manhattan_distance(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                # Calcular la posición X e Y del espacio vacío en el tablero
                x, y = divmod(board[i][j] - 1, 3)
                distance += abs(x - i) + abs(y - j)
    return distance

#Greedy(AnchoPrimeroconheurística)
def GreedySolver(board):
    states = 0
    priority_queue = []
    visited = []
    
    # Guarda en una lista ordenada de menor a mayor, una tupla de la distancia de Manhattan y el tablero
    # Esto evita tener que reordenar la lista cada vez que se agrega un nuevo tablero
    heapq.heappush(priority_queue, (manhattan_distance(board), board))
    
    while priority_queue:
        heuristic_value, current = heapq.heappop(priority_queue)
        states += 1
        print(states)
        
        if current == goal:
            print("Goal found")
            return
        
        if current in visited:
            continue
        
        visited.append(current)
        
        for child in get_children(current):
            if child not in visited:
                heapq.heappush(priority_queue, (manhattan_distance(child), child))
