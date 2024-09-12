from gamebuilder import build_gameboard
from idsSolver import IdsSolver
from idsStarSolver import IdsStarSolver
from greedySolver import GreedySolver
from bfsSolver import BfsSolver
from bfsSolver import get_children
import time

def is_solvable(numbers):
    inversions = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j] and numbers[i] != 0 and numbers[j] != 0:
                inversions += 1
    return inversions % 2 == 0

def main():
  gameboard = build_gameboard()
  while not is_solvable([item for sublist in gameboard for item in sublist]):
    gameboard = build_gameboard()
  start_time = time.time()
  # Cambiar con cada solver
  BfsSolver([[1, 0, 3], [4, 5, 6], [7, 8, 2]])
  print("--- %s seconds ---" % (time.time() - start_time))  

if __name__ == "__main__":
  main()
