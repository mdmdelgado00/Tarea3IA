import heapq
from gamebuilder import get_children, manhattan_distance

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

#Greedy(AnchoPrimeroconheurística)
def GreedySolver(board):
    priority_queue = []
    # Set para guardar estados visitados y no repetirlos
    visited = set()
    
    # Guarda en una lista ordenada de menor a mayor, una tupla de la distancia de Manhattan y el tablero
    # Esto evita tener que reordenar la lista cada vez que se agrega un nuevo tablero
    heapq.heappush(priority_queue, (manhattan_distance(board), board))
    
    while priority_queue:
        heuristic_value, current = heapq.heappop(priority_queue)

        if current == goal:
            print("Goal found")
            return
        
        # Lista de listas a tupla de tuplas para poder utilizar un set
        start_tuple = tuple(tuple(row) for row in board)

        if start_tuple in visited:
            continue
        
        visited.add(start_tuple)
        
        for child in get_children(current):
            child_tuple = tuple(tuple(row) for row in child)
            if child_tuple not in visited:
                heapq.heappush(priority_queue, (manhattan_distance(child), child))
