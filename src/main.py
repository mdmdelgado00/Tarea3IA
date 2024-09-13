from gamebuilder import build_gameboard
from idsSolver import IdsSolver
from idsStarSolver import IdsStarSolver
from greedySolver import GreedySolver
from bfsSolver import BfsSolver
from bfsSolver import get_children
import time
import tracemalloc

def is_solvable(numbers):
  inversions = 0
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      if numbers[i] > numbers[j] and numbers[i] != 0 and numbers[j] != 0:
        inversions += 1
  return inversions % 2 == 0

def main():
  runs = 20
  time_sum = 0
  peak_memory_avg = 0
  for i in range(runs):
    gameboard = build_gameboard()
    while not is_solvable([item for sublist in gameboard for item in sublist]):
      gameboard = build_gameboard()
    
    tracemalloc.start()
    start_time = time.time()

    print("Puzzle " + str(i+1) + ":")
    print()
    for row in gameboard:
      print(row)

    # Cambiar con cada solver
    BfsSolver(gameboard)
    print ("--- Puzzle " + str(i+1) + " solved --- in + " + str(time.time() - start_time) + " seconds ---")
    time_sum += time.time() - start_time
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"Current memory usage is {current / 10**6} MB")
    print(f"Peak memory usage was {peak / 10**6} MB")
    peak_memory_avg += peak / 10**6


  print("Average time: " + str(time_sum/runs))
  print("Average peak memory: " + str(peak_memory_avg/runs))


if __name__ == "__main__":
  main()
