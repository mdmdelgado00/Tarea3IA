from gamebuilder import build_gameboard
from idsSolver import IdsSolver
from idsStarSolver import IdsStarSolver
from greedySolver import GreedySolver
from bfsSolver import BfsSolver
import time

def main():
  gameboard = build_gameboard()
  start_time = time.time() 
  BfsSolver(gameboard)
  print("--- %s seconds ---" % (time.time() - start_time))  

if __name__ == "__main__":
  main()
