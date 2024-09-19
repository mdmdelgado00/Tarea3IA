import heapq
from gamebuilder import get_children, manhattan_distance

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

#Greedy(AnchoPrimeroconheurística)
def GreedySolver(board):
    priority_queue = []
    # Set para guardar estados visitados y no repetirlos
    visited = set()
    
    # Guarda en una lista ordenada de menor a mayor, una tupla de el nivel de nodo, la distancia de Manhattan y el tablero
    # Esto evita tener que reordenar la lista cada vez que se agrega un nuevo tablero
    # Se va a sacar el nodo con el menor nivel, y para nodos con el mismo nivel se sacan basado en su distancia de Manhattan
    # Esto garantiza un breadth first search y para los nodos del mismo nivel se utiliza la heurística
    heapq.heappush(priority_queue, (0, manhattan_distance(board), board))
    
    while priority_queue:
        depth, heuristic_value, current = heapq.heappop(priority_queue)

        if current == goal:
            print("Goal found")
            return
        
        # Lista de listas a tupla de tuplas para poder utilizar un set
        current_tuple = tuple(tuple(row) for row in current)

        if current_tuple in visited:
            continue
        
        visited.add(current_tuple)
        
        for child in get_children(current):
            child_tuple = tuple(tuple(row) for row in child)
            if child_tuple not in visited:
                heapq.heappush(priority_queue, (depth + 1, manhattan_distance(child), child))
